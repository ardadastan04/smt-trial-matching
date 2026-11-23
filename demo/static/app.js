"use strict";
// Demo UI: drives demo/server.py turn by turn and shows what the agent and Z3 do.

const $ = (s, el = document) => el.querySelector(s);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const f2 = (x) => (x == null ? "–" : Number(x).toFixed(2));
const DELAYS = [2800, 1800, 1100, 600, 220]; // ms between question and answer, per speed step

const S = { sid: null, mode: "sim", qid: null, agents: {}, playing: false, busy: false, waiting: null };

async function api(path, body) {
  const r = await fetch(path, body === undefined ? {} : {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body),
  });
  const data = await r.json();
  if (!r.ok) throw new Error(data.error || r.statusText);
  return data;
}

const delay = () => DELAYS[Number($("#speed").value)];

// ------------------------------------------------------------------ captions

function caption(num, html) {
  const el = $("#caption");
  el.innerHTML = (num ? `<span class="cnum">${num}</span>` : "") + `<div>${html}</div>`;
  // a taller caption shrinks the chats; keep them pinned to their latest message
  requestAnimationFrame(() => document.querySelectorAll(".chat").forEach((c) => { c.scrollTop = c.scrollHeight; }));
}

function introCaption() {
  const n = Object.values(S.agents)[0].view.trials.length;
  if (S.mode === "sim") {
    caption("", `This patient has <b>${n} candidate trials</b>, and every trial's criteria have been compiled into Z3 programs. ` +
      `Both agents will interview the same simulated patient: <b>ours</b> (left) and the <b>greedy SMT baseline</b> (right). ` +
      `Press <b>Step</b> or <b>Autoplay</b>, or open <b>How it works</b>.`);
  } else {
    caption("", `You play the patient. Our agent will ask about one fact at a time across <b>${n} trials</b>. ` +
      `Answer Yes, No or Not sure, and watch Z3 update each trial's status. Press <b>Step</b> to get the first question.`);
  }
}

function askCaption(qs) {
  const q = qs.ours;
  if (!q) return;
  const c = q.chosen;
  let html = `Ours asks <span class="q">“${esc(q.text)}”</span> about ${esc(q.nct)}`;
  if (c) {
    html += `: the highest <b>P(answered) × value</b> = ${f2(c.p_answered)} × ${f2(c.value)} = <b>${f2(c.score)}</b>.`;
    const skipped = (q.candidates || []).find((r) => r.value > c.value + 0.05 && r.p_answered < c.p_answered);
    if (skipped) {
      html += ` It passes over <span class="q">“${esc(skipped.text)}”</span>, which is worth more (${f2(skipped.value)}) ` +
        `but probably can't be answered (P = ${f2(skipped.p_answered)}).`;
    }
  }
  if (qs.greedy) html += `<br>Greedy asks <span class="q">“${esc(qs.greedy.text)}”</span>: it could decide a trial, but greedy never considers whether the patient knows the answer.`;
  caption(3, html);
}

function answerCaption(res) {
  const r = res.ours;
  if (!r) return;
  const t = r.turn;
  let html;
  let num = 4;
  if (t.answer === null) {
    html = `The patient is <b>not sure</b>. An unknown answer adds nothing to the solver state, so this question was <span class="no">wasted</span>.`;
  } else if (t.status_after !== t.status_before) {
    const tv = r.agent.trials.find((x) => x.nct === t.nct);
    const side = r.trace.find((x) => x.changed);
    const ok = tv.verdict === tv.gold;
    html = `Answer <b>${esc(t.answer_text)}</b>. Z3: ${side ? `${side.side} program now <b>${side.after}</b> (${esc(side.explain)})` : "status recomputed"}. ` +
      `<b>${esc(t.nct)}</b> is now <b>${t.status_after}</b>. Gold label: ${tv.gold} <span class="${ok ? "ok" : "no"}">${ok ? "✓" : "✗"}</span>`;
    num = 2;
  } else {
    const side = r.trace.find((x) => x.changed) || r.trace[0];
    html = `Answer <b>${esc(t.answer_text)}</b> is added as a solver assumption. Z3 re-checks ${esc(t.nct)}'s programs` +
      (side ? `: ${side.side} is <b>${side.after}</b>` : "") + `, and the trial is still <b>${t.status_after}</b>.`;
  }
  const g = res.greedy;
  if (g && g.turn.answer === null) html += `<br>Greedy's question went <span class="no">unanswered</span>: the note doesn't say.`;
  caption(num, html);
}

function finalCaption() {
  const parts = Object.values(S.agents).map((a) => {
    const v = a.view;
    const k = settledAt(a);
    return `<b>${esc(v.name)}</b>: ${v.n_correct}/${v.trials.length} correct after ${v.n_turns} questions ` +
      `(${v.n_unknown} unanswered)` + (k != null ? `, with every final verdict reached by question ${k}` : "");
  });
  caption("✓", parts.join("<br>"));
}

// the question after which the number of correct verdicts never changed again
function settledAt(a) {
  const h = a.history;
  if (!h.length) return null;
  const last = h[h.length - 1];
  let k = h.length;
  while (k > 0 && h[k - 1] === last) k--;
  return k + 1; // h[k] is the first answer after which the count stayed at its final value
}

// ------------------------------------------------------------------ rendering

function buildColumns(view) {
  const box = $("#columns");
  box.innerHTML = "";
  box.classList.toggle("single", S.mode !== "sim");
  S.agents = {};
  for (const [kind, v] of Object.entries(view.agents)) {
    const el = $("#col-tpl").content.firstElementChild.cloneNode(true);
    el.classList.add(kind);
    $(".agent-name", el).textContent = v.name;
    $(".rank-help", el).textContent = kind === "ours"
      ? "Score = P(the patient can answer) × value of the answer. Value is the chance the answer rules out a trial, a cohort, or settles eligibility."
      : "Greedy scores 2 points for each yes/no answer that would decide a trial, +1 for a yes/no question. It ignores answerability.";
    box.appendChild(el);
    S.agents[kind] = { el, view: v, history: [], lastNct: null };
    renderAgent(kind, v);
    renderRank(kind, null);
  }
}

function renderAgent(kind, v, flash = {}) {
  const a = S.agents[kind];
  const prev = a.view;
  a.view = v;
  const el = a.el;
  const set = (k, val) => el.querySelectorAll(`[data-k="${k}"]`).forEach((n) => {
    if (n.textContent !== String(val) && n.textContent !== "") n.parentElement.classList.remove("bump"), void n.offsetWidth, n.parentElement.classList.add("bump");
    n.textContent = val;
  });
  set("turns", v.n_turns); set("unknown", v.n_unknown); set("decided", v.n_decided);
  set("correct", v.n_correct); set("n", v.trials.length);
  $(".trials", el).innerHTML = v.trials.map((t) => trialHtml(t, flash[t.nct], a.lastNct === t.nct)).join("");
  void prev;
}

function trialHtml(t, flash, focus) {
  const coh = t.cohorts.map((c) =>
    `<span class="coh">${t.cohorts.length > 1 ? `<span class="cid">${esc(c.id)}</span>` : ""}` +
    `incl <span class="side-dot ${c.inclusion}">${c.inclusion}</span> ` +
    `excl <span class="side-dot ${c.exclusion}">${c.exclusion}</span></span>`).join("");
  const ok = t.verdict === t.gold;
  return `<div class="trial ${focus ? "focus" : ""} ${flash ? `flash-${flash}` : ""}">
    <div class="tt"><span class="nct">${esc(t.nct)}</span>${esc(t.title)}</div>
    <span class="status ${t.status}">${t.status}</span>
    <div class="sub"><span class="cohorts">${coh}</span>
      <span>${t.n_asked} asked</span>
      <span class="verdict">verdict <b>${t.verdict}</b> · gold ${t.gold} <span class="${ok ? "ok" : "no"}">${ok ? "✓" : "✗"}</span></span>
    </div></div>`;
}

const outcome = (s) => (s ? `<span class="out ${s}">${s === "undetermined" ? "open" : s}</span>` : "–");
const bar = (x, max, cls = "") => `<div class="bar ${cls}"><span style="width:${Math.max(0, Math.min(1, x / max)) * 100}%"></span><em>${f2(x)}</em></div>`;

function renderRank(kind, q) {
  const el = $(".rank", S.agents[kind].el);
  const sub = $(".rank-sub", S.agents[kind].el);
  if (!q) { el.innerHTML = `<div class="empty">The candidate questions and their scores show up here.</div>`; sub.textContent = ""; return; }
  sub.textContent = `top ${q.candidates.length} of ${q.n_candidates} open questions`;
  const rows = q.candidates;
  const max = Math.max(...rows.map((r) => r.score), 1e-9);
  const isChosen = (r) => r.nct === q.nct && r.var === q.var;
  const label = (r) => `<td class="q" title="${esc(r.var)}"><span class="nct">${esc(r.nct.slice(-4))}</span>${esc(r.text)}</td>`;
  if (kind === "ours") {
    el.innerHTML = `<table><colgroup><col><col style="width:78px"><col style="width:48px"><col style="width:78px"></colgroup>
      <tr><th>question</th><th>P(answered)</th><th>value</th><th>score</th></tr>
      ${rows.map((r) => `<tr class="${isChosen(r) ? "chosen" : ""}">${label(r)}
        <td>${bar(r.p_answered, 1, "pans")}</td><td>${f2(r.value)}</td><td>${bar(r.score, max)}</td></tr>`).join("")}</table>`;
  } else {
    el.innerHTML = `<table><colgroup><col><col style="width:70px"><col style="width:70px"><col style="width:50px"></colgroup>
      <tr><th>question</th><th>if yes →</th><th>if no →</th><th>score</th></tr>
      ${rows.map((r) => `<tr class="${isChosen(r) ? "chosen" : ""}">${label(r)}
        <td>${outcome(r.if_yes)}</td><td>${outcome(r.if_no)}</td><td>${r.score}</td></tr>`).join("")}</table>`;
  }
}

function renderTrace(kind, res) {
  const el = $(".trace", S.agents[kind].el);
  const t = res.turn;
  const head = `<div class="assign">${esc(t.nct)}: <b>${esc(t.var)}</b> = ${t.answer === null ? "<i>unknown (no assumption added)</i>" : esc(JSON.stringify(t.answer))}</div>`;
  if (t.answer === null) { el.innerHTML = head + `<div class="tr-explain">The solver state is unchanged; every program keeps its previous status.</div>`; return; }
  const re = new RegExp(t.var.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g");
  el.innerHTML = head + res.trace.slice(0, 3).map((r) => `<div class="tr-row ${r.changed ? "changed" : ""}">
    <div class="tr-head"><b>${r.cohort === "main" ? "" : `cohort ${esc(r.cohort)} · `}${r.side}</b>
      <span class="side-dot ${r.before}">${r.before}</span><span class="arrow">→</span><span class="side-dot ${r.after}">${r.after}</span></div>
    <div class="tr-explain">${esc(r.explain)}</div>
    ${r.assertions.slice(0, 1).map((s) => `<div class="smt">${esc(s.length > 320 ? s.slice(0, 320) + " …" : s).replace(re, (m) => `<mark>${m}</mark>`)}</div>`).join("")}
  </div>`).join("");
}

function addMsg(kind, html, cls) {
  const chat = $(".chat", S.agents[kind].el);
  const d = document.createElement("div");
  d.className = cls;
  d.innerHTML = html;
  chat.appendChild(d);
  chat.scrollTop = chat.scrollHeight;
  setTimeout(() => { chat.scrollTop = chat.scrollHeight; }, 300); // again after the pop-in animation
}

function showQuestion(kind, q) {
  S.agents[kind].lastNct = q.nct;
  addMsg(kind, `<span class="meta">Q${q.turn} · ${esc(q.nct)} · ${esc(q.trial_title.slice(0, 60))}</span>${esc(q.text)}<span class="var">${esc(q.var)}</span>`, "msg agent");
  renderRank(kind, q);
  renderAgent(kind, S.agents[kind].view);
}

function showAnswer(kind, res) {
  const t = res.turn;
  const a = S.agents[kind];
  if (t.answer === null) addMsg(kind, "I'm not sure.", "msg patient unknown");
  else addMsg(kind, esc(t.type === "Bool" ? (t.answer ? "Yes." : "No.") : t.answer_text), "msg patient");
  const tv = res.agent.trials.find((x) => x.nct === t.nct);
  if (t.answer === null) {
    addMsg(kind, "⚙ unknown: nothing to add to the solver · wasted question", "sys waste");
  } else if (t.status_after !== t.status_before) {
    const ok = tv.verdict === tv.gold;
    addMsg(kind, `⚙ Z3: ${esc(t.nct)} → <b>${t.status_after}</b> (gold ${tv.gold} ${ok ? "✓" : "✗"})`, `sys ${t.status_after === "ineligible" ? "no" : "ok"}`);
  } else {
    addMsg(kind, `⚙ Z3: ${esc(t.nct)} still ${t.status_after}`, "sys");
  }
  const flash = t.status_after !== t.status_before ? { [t.nct]: t.status_after } : {};
  renderAgent(kind, res.agent, flash);
  renderTrace(kind, res);
  a.history.push(res.agent.n_correct);
}

function markDone(kind) {
  const v = S.agents[kind].view;
  if (S.agents[kind].doneShown) return;
  S.agents[kind].doneShown = true;
  const why = v.n_turns >= 30 ? "Question budget (30) used up." : "No remaining question could change any trial's status, so the agent stops.";
  addMsg(kind, `${why}<br>Final: <b>${v.n_correct}/${v.trials.length}</b> verdicts correct after ${v.n_turns} questions, ${v.n_unknown} unanswered.`, "summary");
}

// ------------------------------------------------------------------ the turn loop

const active = () => Object.keys(S.agents).filter((k) => !S.agents[k].view.done);

async function step() {
  if (S.busy || !S.sid) return;
  const kinds = active();
  if (!kinds.length) return finish();
  S.busy = true; updateButtons();
  try {
    const qs = {};
    for (const k of kinds) {
      const r = await api("/api/ask", { sid: S.sid, agent: k });
      S.agents[k].view = r.agent;
      if (r.question) { qs[k] = r.question; showQuestion(k, r.question); } else markDone(k);
    }
    if (!Object.keys(qs).length) return finish();
    askCaption(qs);
    let values = {};
    if (S.mode === "manual") values = { ours: await waitForUser(qs.ours) };
    else await sleep(delay());
    const res = {};
    for (const k of Object.keys(qs)) {
      res[k] = await api("/api/answer", { sid: S.sid, agent: k, value: values[k] ?? "__sim__" });
      showAnswer(k, res[k]);
      if (res[k].agent.done) markDone(k);
    }
    answerCaption(res);
    if (!active().length) { await sleep(Math.min(delay(), 1200)); finish(); }
  } catch (e) {
    caption("!", `Error: ${esc(e.message)}`);
    S.playing = false;
  } finally {
    S.busy = false; updateButtons();
  }
}

function finish() {
  S.playing = false;
  // agents that have not hit the end yet still need an ask() to learn they are done
  for (const k of Object.keys(S.agents)) markDone(k);
  finalCaption();
  updateButtons();
}

function waitForUser(q) {
  const bar = $(".answer-bar", S.agents.ours.el);
  bar.classList.remove("hidden");
  const hint = `<span class="hintkey" title="What the answer key extracted from the note">note says: <b>${esc(q.key_answer)}</b></span>`;
  bar.innerHTML = q.type === "Bool"
    ? `<button class="primary" data-v="yes">Yes</button><button data-v="no">No</button><button data-v="unknown">Not sure</button>${hint}`
    : `<input type="number" step="any" placeholder="${esc(q.unit || "number")}"><button class="primary" data-v="num">Answer</button><button data-v="unknown">Not sure</button>${hint}`;
  const input = $("input", bar);
  if (input) input.focus();
  return new Promise((resolve) => {
    const done = (v) => { bar.classList.add("hidden"); bar.innerHTML = ""; S.waiting = null; resolve(v); };
    S.waiting = done;
    bar.onclick = (e) => {
      const b = e.target.closest("button");
      if (!b) return;
      if (b.dataset.v === "num") { if (input.value.trim() !== "") done(input.value.trim()); } else done(b.dataset.v);
    };
    if (input) input.onkeydown = (e) => { if (e.key === "Enter" && input.value.trim() !== "") done(input.value.trim()); };
  });
}

async function autoplay() {
  if (S.mode === "manual") return;
  S.playing = !S.playing;
  updateButtons();
  while (S.playing && active().length) {
    await step();
    if (S.playing) await sleep(delay() * 0.7);
  }
  if (!active().length) finish();
  S.playing = false; updateButtons();
}

function updateButtons() {
  const over = S.sid && !active().length;
  $("#btn-step").disabled = S.busy || over || S.playing;
  $("#btn-play").disabled = S.mode === "manual" || over;
  $("#btn-play").textContent = S.playing ? "Pause ❚❚" : "Autoplay ▶";
}

async function start() {
  S.playing = false;
  if (S.waiting) S.waiting("unknown"); // drop a pending manual question
  while (S.busy) await sleep(50);
  const view = await api("/api/start", { qid: $("#patient").value, mode: S.mode });
  S.sid = view.sid; S.qid = view.qid;
  $("#qid").textContent = view.qid;
  $("#note").textContent = view.note;
  buildColumns(view);
  introCaption();
  updateButtons();
}

// ------------------------------------------------------------------ "how it works" tour

const TOUR = [
  { region: "trials", title: "Trials become solver programs",
    body: "Every candidate trial's eligibility criteria were compiled ahead of time into SMT-LIB programs, one inclusion and one exclusion program per cohort. Z3 tracks each program as <b>satisfied</b>, <b>violated</b> or <b>open</b>." },
  { region: "chat", title: "One fact per question",
    body: "The agent asks about one variable at a time, such as <code>patient_is_pregnant_now</code>, phrased in plain English. Every answer becomes an assumption <code>A</code> in the solver; “not sure” adds nothing." },
  { region: "trace", title: "Two satisfiability checks per program",
    body: "With background facts <code>B</code>, answers <code>A</code> and criteria <code>C</code>: if <code>B∧A∧C</code> is UNSAT, a criterion already fails (<b>violated</b>). If <code>B∧A∧¬C</code> is UNSAT, the criteria hold however the unknowns turn out (<b>satisfied</b>). Otherwise the program is <b>open</b>." },
  { region: "rank", title: "Choosing the next question",
    body: "Greedy SMT asks any question whose answer could decide a trial. But about two thirds of program variables aren't in the patient's notes, so many of those questions go unanswered. <b>Ours</b> scores each question by <b>P(answered) × value</b>, with P(answered) predicted from the variable name and fit on dev patients only." },
  { region: "score", title: "Verdicts and scoring",
    body: "A trial is ineligible once every cohort is violated, and certainly eligible once some cohort is satisfied. When the conversation stops, undetermined trials count as eligible. We compare each verdict with the TREC gold label and count unanswered questions." },
];
let tourAt = 0;

function tourShow(i) {
  tourAt = Math.max(0, Math.min(TOUR.length - 1, i));
  const t = TOUR[tourAt];
  document.querySelectorAll(".spot").forEach((n) => n.classList.remove("spot"));
  const target = document.querySelector(`.col.ours [data-region="${t.region}"]`);
  if (target) target.classList.add("spot");
  $("#tour").classList.remove("hidden");
  $("#tour-step").textContent = `How it works · ${tourAt + 1} of ${TOUR.length}`;
  $("#tour-title").textContent = t.title;
  $("#tour-body").innerHTML = t.body;
  $("#tour-dots").innerHTML = TOUR.map((_, j) => `<span class="${j === tourAt ? "on" : ""}"></span>`).join("");
  $("#tour-prev").disabled = tourAt === 0;
  $("#tour-next").textContent = tourAt === TOUR.length - 1 ? "Done ✓" : "Next ▸";
  caption(String(["2", "1", "4", "3", "✓"][tourAt]), `<b>${esc(t.title)}.</b> ${t.body}`);
}

function tourClose() {
  $("#tour").classList.add("hidden");
  document.querySelectorAll(".spot").forEach((n) => n.classList.remove("spot"));
  introCaption();
}

// ------------------------------------------------------------------ wiring

async function init() {
  const { patients, default: def } = await api("/api/patients");
  $("#patient").innerHTML = patients.map((p) =>
    `<option value="${p.qid}" ${p.qid === def ? "selected" : ""}>${p.qid} · ${p.n_trials} trial${p.n_trials > 1 ? "s" : ""} · ${esc(p.summary.slice(0, 60))}</option>`).join("");
  $("#patient").onchange = start;
  const setMode = (m) => {
    S.mode = m;
    $("#mode-sim").classList.toggle("on", m === "sim");
    $("#mode-manual").classList.toggle("on", m === "manual");
    start();
  };
  $("#mode-sim").onclick = () => setMode("sim");
  $("#mode-manual").onclick = () => setMode("manual");
  $("#btn-step").onclick = step;
  $("#btn-play").onclick = autoplay;
  $("#btn-reset").onclick = start;
  $("#btn-tour").onclick = () => tourShow(0);
  $("#tour-prev").onclick = () => tourShow(tourAt - 1);
  $("#tour-next").onclick = () => (tourAt === TOUR.length - 1 ? tourClose() : tourShow(tourAt + 1));
  $("#captions").onchange = (e) => $("#caption").classList.toggle("off", !e.target.checked);
  $("#note-toggle").onclick = (e) => {
    const clamped = $("#note").classList.toggle("clamp");
    e.target.textContent = clamped ? "show full note" : "hide note";
  };
  document.addEventListener("keydown", (e) => {
    if (e.target.matches("input, select")) return;
    const tourOpen = !$("#tour").classList.contains("hidden");
    if (tourOpen && (e.key === "ArrowRight" || e.key === "Enter")) { e.preventDefault(); $("#tour-next").click(); return; }
    if (tourOpen && e.key === "ArrowLeft") { tourShow(tourAt - 1); return; }
    if (e.key === "Escape") { tourClose(); return; }
    if (e.key === " ") { e.preventDefault(); step(); }
    else if (e.key === "a") autoplay();
    else if (e.key === "r") start();
    else if (e.key === "h") tourShow(0);
    else if (e.key === "c") $("#captions").click();
  });
  await start();
}

init().catch((e) => caption("!", `Could not start: ${esc(e.message)}. Is demo/server.py running?`));
