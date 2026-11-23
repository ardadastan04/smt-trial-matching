"""Turn a trial variable name into a plain-English question (templates only, no LLM).

Variable names follow a loose grammar: ``<subject>_<relation>_<concept>_<time>``, e.g.
``patient_has_diagnosis_of_asthma_now`` or ``patient_age_value_recorded_now_in_years``. We strip the
time suffix, match the relation against a small table of templates, and fall back to the variable's
``meaning`` (or the de-snaked name) when nothing matches. Numbers get "What is your ...?" plus a unit.
"""

from __future__ import annotations

import re

# (time suffix regex, phrase used in the question); first match wins
_TIME = [
    (r"_inthepast_?(\d+)_?(day|week|month|year)s?$", None),  # handled specially below
    (r"_inthefuture_?(\d+)_?(day|week|month|year)s?$", None),
    (r"_(now|currently)$", "now"),
    (r"_(inthehistory|in_the_history|in_the_past|ever)$", "ever"),
]

# (prefix, template for "now", template for "ever"); {x} is the concept
_BOOL = [
    ("patient_has_diagnosis_of_", "Have you been diagnosed with {x}?", "Have you ever been diagnosed with {x}?"),
    ("patient_has_finding_of_", "Do you currently have {x}?", "Have you ever had {x}?"),
    ("patient_has_symptoms_of_", "Do you currently have symptoms of {x}?", "Have you ever had symptoms of {x}?"),
    ("patient_has_suspicion_of_", "Is {x} suspected right now?", "Has {x} ever been suspected?"),
    ("patient_has_history_of_", "Do you have a history of {x}?", "Do you have a history of {x}?"),
    ("patient_has_family_history_of_", "Does anyone in your family have {x}?", "Does anyone in your family have {x}?"),
    ("patient_has_allergy_to_", "Are you allergic to {x}?", "Have you ever had an allergy to {x}?"),
    ("patient_has_hypersensitivity_to_", "Are you hypersensitive to {x}?",
     "Have you ever had a hypersensitivity reaction to {x}?"),
    ("patient_has_contraindication_to_", "Is there any reason you can't receive {x}?",
     "Has {x} ever been ruled out for you?"),
    ("patient_has_undergone_", "Have you had {x}?", "Have you ever had {x}?"),
    ("patient_has_received_", "Have you received {x}?", "Have you ever received {x}?"),
    ("patient_has_taken_", "Have you taken {x}?", "Have you ever taken {x}?"),
    ("patient_has_been_", "Have you been {x}?", "Have you ever been {x}?"),
    ("patient_has_", "Do you have {x}?", "Have you ever had {x}?"),
    ("patient_is_undergoing_", "Are you currently receiving {x}?", "Have you ever received {x}?"),
    ("patient_is_exposed_to_", "Are you currently taking or exposed to {x}?", "Have you ever taken or been exposed to {x}?"),
    ("patient_is_taking_", "Are you currently taking {x}?", "Have you ever taken {x}?"),
    ("patient_is_using_", "Are you currently using {x}?", "Have you ever used {x}?"),
    ("patient_is_able_to_", "Are you able to {x}?", "Have you been able to {x}?"),
    ("patient_is_unable_to_", "Are you unable to {x}?", "Have you been unable to {x}?"),
    ("patient_is_willing_to_", "Are you willing to {x}?", "Are you willing to {x}?"),
    ("patient_is_unwilling_to_", "Would you be unwilling to {x}?", "Would you be unwilling to {x}?"),
    ("patient_is_", "Are you {x}?", "Have you ever been {x}?"),
    ("patient_can_", "Can you {x}?", "Can you {x}?"),
    ("patient_will_", "Are you going to {x}?", "Are you going to {x}?"),
    ("patient_needs_to_", "Do you need to {x}?", "Do you need to {x}?"),
    ("patient_requires_", "Do you need {x}?", "Do you need {x}?"),
    ("patient_meets_", "Do you meet the {x}?", "Have you met the {x}?"),
    ("patient_sex_is_", "Is your sex {x}?", "Is your sex {x}?"),
]

_UNITS = {
    "years": "years", "months": "months", "weeks": "weeks", "days": "days", "hours": "hours",
    "kilograms": "kg", "kg": "kg", "kg_per_m2": "kg/m²", "mm_hg": "mmHg", "percent": "%",
    "u_per_l": "U/L", "ml_per_min": "mL/min", "liter": "L", "centimeter": "cm", "mg_per_dl": "mg/dL",
}

_FILLER = re.compile(r"_(value_recorded|value|recorded|measure|level|finding)(?=_|$)")


def words(s: str) -> str:
    """snake_case -> words, with the common ``parkinson_s`` possessive repaired."""
    s = s.replace("@@", " ").replace("_s_", "'s ")
    return re.sub(r"\s+", " ", s.replace("_", " ")).strip()


def _split_time(name: str) -> tuple[str, str]:
    """(name without its time suffix, 'now' | 'ever' | phrase like 'in the past 6 months')."""
    for pat, tag in _TIME:
        m = re.search(pat, name)
        if not m:
            continue
        if tag is None:
            n, unit = m.group(1), m.group(2)
            past = "inthepast" in pat
            phrase = f"in the past {n} {unit}{'s' if n != '1' else ''}" if past else \
                f"in the next {n} {unit}{'s' if n != '1' else ''}"
            return name[: m.start()], phrase
        return name[: m.start()], tag
    return name, "now"


def unit_of(name: str) -> str:
    """Display unit of a numeric variable, from its ``_withunit_X`` / ``_in_X`` suffix ('' if none)."""
    m = re.search(r"_withunit_([a-z0-9_]+)$", name) or re.search(r"_in_(years|months|weeks|days|hours|kilograms)$", name)
    if not m:
        return ""
    u = m.group(1)
    return _UNITS.get(u, words(u))


def numeric_question(name: str) -> str:
    name = name.split("@@")[0]
    base = re.sub(r"_withunit_[a-z0-9_]+$", "", name)
    base = re.sub(r"_in_(years|months|weeks|days|hours|kilograms)$", "", base)
    base = re.sub(r"_(now|inthehistory)(?=_|$)", "", base)
    base = _FILLER.sub("", base)
    base = re.sub(r"^patient_(finding_of_)?", "", base)
    thing = words(base) or words(name)
    if thing == "age":
        thing = "current age"
    unit = unit_of(name)
    return f"What is your {thing}{f' (in {unit})' if unit else ''}?"


def bool_question(name: str, meaning: str = "") -> str:
    core, when = _split_time(name.split("@@")[0])
    # every qualifier, not just the first: "...@@extensive@@caused_by_burns" and "...@@caused_by_sloughing"
    # are different variables and must not read as the same question
    qualifier = ", ".join(words(q) for q in name.split("@@")[1:])
    for prefix, now_t, ever_t in _BOOL:
        if core.startswith(prefix) and len(core) > len(prefix):
            x = words(core[len(prefix):])
            lead = prefix.removeprefix("patient_has_").removeprefix("patient_is_").replace("_", " ").strip()
            if lead and x.startswith(lead + " "):  # "allergy to allergy to X" -> "allergy to X"
                x = x[len(lead) + 1:]
            if when in ("now", "ever"):
                q = (now_t if when == "now" else ever_t).format(x=x)
            else:
                q = ever_t.format(x=x).replace(" ever ", " ").rstrip("?") + f" {when}?"
            if qualifier:
                q = q.rstrip("?") + f" ({qualifier})?"
            return q
    if meaning:
        m = re.sub(r"^(boolean|bool)( value)? (indicating|representing) (whether|if) ", "", meaning.strip(),
                   flags=re.IGNORECASE).rstrip(".")
        return f"Is this true for you: {m}?"
    return f"Is this true for you: {words(name)}?"


def question_text(name: str, vtype: str, meaning: str = "") -> str:
    """Plain-English question for one variable (Bool -> yes/no, Int/Real -> a number)."""
    return bool_question(name, meaning or "") if vtype == "Bool" else numeric_question(name)
