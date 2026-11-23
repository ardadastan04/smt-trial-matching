"""Local demo server: the conversational trial-matching agent with what it does behind the scenes.

  uv run python demo/server.py            # then open http://localhost:8000
  uv run python demo/server.py --port 8010 --qid trec-202161

Standard library only (no new dependencies), single-threaded (Z3 objects are not shared across
threads), local only: it binds 127.0.0.1 because the pages show TREC patient notes.

API (JSON over POST, one live session per browser tab, keyed by ``sid``):
  GET  /api/patients                          dev patients for the picker
  POST /api/start   {qid, mode}               -> {sid, session view}
  POST /api/ask     {sid, agent}              -> next question + ranked candidates (or null when done)
  POST /api/answer  {sid, agent, value}       -> solver trace + updated agent view; value "__sim__" = answer key
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "src")]

from demo.engine import DemoSession, dev_patients

STATIC = Path(__file__).resolve().parent / "static"
TYPES = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
         ".css": "text/css; charset=utf-8", ".svg": "image/svg+xml"}
SESSIONS: dict[str, DemoSession] = {}
_ids = itertools.count(1)
DEFAULT_QID = "trec-202139"


def handle(path: str, body: dict) -> object:
    if path == "/api/start":
        s = DemoSession(body.get("qid") or DEFAULT_QID, body.get("mode", "sim"))
        sid = str(next(_ids))
        SESSIONS.clear()  # one live demo at a time keeps memory flat
        SESSIONS[sid] = s
        return {"sid": sid, **s.view()}
    s = SESSIONS.get(str(body.get("sid")))
    if s is None:
        raise KeyError("session expired; press Reset")
    agent = s.agents[body.get("agent", "ours")]
    if path == "/api/ask":
        return {"question": agent.ask(), "agent": agent.view()}
    if path == "/api/answer":
        return agent.answer(body.get("value", "__sim__"))
    raise FileNotFoundError(path)


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, data: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _json(self, code: int, obj: object) -> None:
        self._send(code, json.dumps(obj).encode(), "application/json")

    def do_GET(self) -> None:
        if self.path == "/api/patients":
            return self._json(200, {"patients": dev_patients(), "default": DEFAULT_QID})
        rel = "index.html" if self.path in ("/", "") else self.path.lstrip("/").split("?")[0]
        f = (STATIC / rel).resolve()
        if STATIC not in f.parents or not f.is_file():
            return self._send(404, b"not found", "text/plain")
        self._send(200, f.read_bytes(), TYPES.get(f.suffix, "application/octet-stream"))

    def do_POST(self) -> None:
        n = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
            self._json(200, handle(self.path, body))
        except (KeyError, ValueError, RuntimeError) as e:
            self._json(400, {"error": str(e)})
        except FileNotFoundError:
            self._json(404, {"error": "unknown endpoint"})
        except Exception as e:  # noqa: BLE001 -- keep the demo alive; show the error in the UI
            traceback.print_exc()
            self._json(500, {"error": f"{type(e).__name__}: {e}"})

    def log_message(self, fmt: str, *args: object) -> None:
        if "/api/" in (args[0] if args else ""):
            return  # quiet: one line per turn is noise during a recording
        super().log_message(fmt, *args)


def main(argv: list[str] | None = None) -> int:
    global DEFAULT_QID
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--qid", default=DEFAULT_QID, help="patient preselected in the picker (dev only)")
    a = ap.parse_args(argv)
    DEFAULT_QID = a.qid
    srv = HTTPServer(("127.0.0.1", a.port), Handler)
    print(f"Demo running at http://localhost:{a.port}  (Ctrl-C to stop)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
