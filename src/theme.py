"""Custom CSS + reusable HTML snippets to make the Streamlit app look distinctive.

✅ PROVIDED — you don't need to edit this file. It's the styling for app.py.
"""
from __future__ import annotations

import streamlit as st


CUSTOM_CSS = """
<style>
/* ---------- App-wide tone ---------- */
:root {
  --accent: #7c5cff;
  --accent-2: #008f72;
  --accent-warn: #a96600;
  --accent-bad: #b93660;
  --panel: #ffffff;
  --panel-strong: #edf3f0;
  --border: #d7e1dc;
  --text-muted: #65756f;
  --background-color: #f4f7f5;
  --secondary-background-color: #ffffff;
  --text-color: #263431;
  color-scheme: light;
}

html, body, [class*="css"] {
  font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, sans-serif !important;
  color: #263431;
}

.stApp {
  background:
    radial-gradient(1200px 600px at 10% -10%, rgba(124,92,255,0.08), transparent 60%),
    radial-gradient(1000px 500px at 100% 0%, rgba(0,143,114,0.08), transparent 60%),
    #f4f7f5 !important;
  color: #263431 !important;
}

[data-testid="stAppViewContainer"], [data-testid="stMain"] {
  color: #263431 !important;
}

.stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stWidgetLabel"],
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stText"],
.stApp label,
.stApp p,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp li {
  color: #263431;
}

/* Hide default Streamlit chrome we don't need */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* ---------- Hero ---------- */
.hero {
  padding: 26px 28px 20px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: linear-gradient(120deg, #ffffff 15%, #edf7f3 100%);
  margin-bottom: 18px;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 4px;
  background: linear-gradient(180deg, #7c5cff, #008f72);
  pointer-events: none;
}
.hero h1 {
  font-size: 34px;
  margin: 0 0 6px 0;
  background: linear-gradient(90deg, #3e347c, #08745d);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-weight: 700;
}
.hero p {
  color: #4b5c57;
  margin: 0;
  font-size: 15px;
  line-height: 1.55;
  max-width: 760px;
}
.hero .badges {
  margin-top: 12px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.badge {
  font-size: 11px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 6px;
  background: #f0edff;
  color: #51429d;
  border: 1px solid #d8d0ff;
}
.badge.green { background: #e6f5ee; color: #17684f; border-color: #b7dfcc; }
.badge.warn  { background: #fff3dc; color: #805000; border-color: #f1d49a; }

/* ---------- Agent cards ---------- */
.agent-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin: 8px 0 4px; }
.agent {
  position: relative;
  padding: 14px 16px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--panel);
  transition: all 0.3s ease;
}
.agent.active {
  background: linear-gradient(135deg, #f1edff, #eaf7f1);
  border-color: #a99ae8;
  box-shadow: 0 2px 10px rgba(56,74,67,0.08);
  transform: translateY(-2px);
}
.agent.done {
  background: #eaf6ef;
  border-color: #acd8c0;
}
.agent .role {
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
}
.agent .name {
  font-size: 17px;
  font-weight: 700;
  color: #263431;
  margin: 2px 0 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.agent .desc {
  font-size: 13px;
  color: #52625d;
  line-height: 1.45;
}
.agent .status {
  margin-top: 10px;
  font-size: 12px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}
.dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: #555;
  display: inline-block;
}
.agent.active .dot {
  background: var(--accent);
  box-shadow: 0 0 0 0 rgba(124,92,255, 0.35);
  animation: pulse 1.6s infinite;
}
.agent.done .dot { background: var(--accent-2); }
@keyframes pulse {
  0%   { box-shadow: 0 0 0 0 rgba(124,92,255, 0.35); }
  70%  { box-shadow: 0 0 0 10px rgba(124,92,255, 0); }
  100% { box-shadow: 0 0 0 0 rgba(124,92,255, 0); }
}

/* ---------- Verdict pill in memo ---------- */
.verdict {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 8px 14px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 14px;
  margin: 4px 0 12px;
  border: 1px solid;
}
.verdict.go   { background: #e6f5ee; color: #17684f; border-color: #b7dfcc; }
.verdict.pivot{ background: #fff3dc; color: #805000; border-color: #f1d49a; }
.verdict.pass { background: #fcebf0; color: #9b3155; border-color: #edbdcc; }

/* ---------- Buttons ---------- */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button {
  border-radius: 10px !important;
  font-weight: 600 !important;
  color: #263431 !important;
  transition: transform 0.1s ease, box-shadow 0.2s ease !important;
}
.stFormSubmitButton > button[kind="primary"] {
  background: linear-gradient(135deg, #6655c9, #5142aa) !important;
  border: none !important;
  color: #ffffff !important;
  box-shadow: 0 4px 12px -4px rgba(81,66,170,0.35) !important;
}
.stFormSubmitButton > button[kind="primary"]:hover {
  transform: translateY(-1px);
  box-shadow: 0 7px 16px -4px rgba(81,66,170,0.45) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] {
  gap: 6px;
  background: transparent;
}
.stTabs [data-baseweb="tab"] {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
  padding: 8px 16px !important;
  color: #52625d !important;
  font-weight: 500;
}
.stTabs [aria-selected="true"] {
  background: #eeebff !important;
  border-color: #c8bfff !important;
  color: #423783 !important;
}

/* ---------- Inputs ---------- */
.stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
  background: #ffffff !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
  color: #263431 !important;
}
.stTextArea textarea::placeholder, .stTextInput input::placeholder {
  color: #65756f !important;
  opacity: 1;
}
.stSelectbox [data-baseweb="select"] * {
  color: #263431 !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 2px rgba(124,92,255,0.12) !important;
}

/* ---------- Sidebar polish ---------- */
section[data-testid="stSidebar"] {
  background: #edf2ef !important;
  border-right: 1px solid var(--border);
}

/* ---------- Status / code log ---------- */
.stCode, pre {
  border-radius: 10px !important;
  font-size: 12px !important;
}

/* ---------- Result card ---------- */
.result-card {
  padding: 18px 22px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--panel);
  margin-bottom: 12px;
}
.result-card .title {
  font-size: 13px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 4px;
}
.result-card .idea {
  font-size: 20px;
  font-weight: 700;
  color: #263431;
  line-height: 1.3;
}

/* Subtle scrollbars */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-thumb { background: #c5d0cb; border-radius: 6px; }
::-webkit-scrollbar-thumb:hover { background: #aebdb6; }
</style>
"""


def inject_css() -> None:
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def hero(gemini_ok: bool) -> None:
    key_badge = (
        '<span class="badge green">● Gemini connected</span>'
        if gemini_ok
        else '<span class="badge warn">! Add GEMINI_API_KEY</span>'
    )
    st.markdown(
        f"""
        <div class="hero">
          <h1>🎯 Startup Idea Validator</h1>
          <p>Three opinionated AI agents — <strong>🚀 Optimist</strong>,
          <strong>🔪 Skeptic</strong>, <strong>🎯 Strategist</strong> — debate
          your idea and deliver a decision-grade memo with a verdict, the riskiest
          assumption, a 90-day MVP scope, and kill criteria.</p>
          <div class="badges">
            <span class="badge">Powered by CrewAI</span>
            <span class="badge">DuckDuckGo Search · No key needed</span>
            {key_badge}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def agent_cards(active: str | None = None, done: set[str] | None = None) -> None:
    """Render the three agent cards with active/done states.

    active: one of {"optimist","skeptic","strategist"} or None
    done:   set of agents that have finished
    """
    done = done or set()

    def state(name: str) -> str:
        if name in done:
            return "done"
        if name == active:
            return "active"
        return ""

    def status_text(name: str) -> str:
        if name in done:
            return "✓ Done"
        if name == active:
            return "● Working…"
        return "Idle"

    st.markdown(
        f"""
        <div class="agent-row">
          <div class="agent {state('optimist')}">
            <div class="role">Agent 1 · Bull Case</div>
            <div class="name">🚀 The Optimist</div>
            <div class="desc">Ex-VC who hunts tailwinds, market signals,
            customer demand evidence, and comparable winners.</div>
            <div class="status"><span class="dot"></span>{status_text('optimist')}</div>
          </div>
          <div class="agent {state('skeptic')}">
            <div class="role">Agent 2 · Bear Case</div>
            <div class="name">🔪 The Skeptic</div>
            <div class="desc">Serial founder with scars. Finds incumbents,
            failed predecessors, distribution traps, and apathy risks.</div>
            <div class="status"><span class="dot"></span>{status_text('skeptic')}</div>
          </div>
          <div class="agent {state('strategist')}">
            <div class="role">Agent 3 · Synthesis</div>
            <div class="name">🎯 The Strategist</div>
            <div class="desc">YC-style partner. Weighs evidence and writes the
            decision memo: verdict, riskiest assumption, MVP, kill criteria.</div>
            <div class="status"><span class="dot"></span>{status_text('strategist')}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def detect_verdict(memo_md: str) -> tuple[str, str] | None:
    """Return (css_class, label) tuple if a verdict is found in the memo."""
    lower = memo_md.lower()
    # Look in the first ~800 chars to avoid false positives
    head = lower[:800]
    if "🟢" in memo_md[:800] or "pursue" in head:
        return ("go", "🟢 PURSUE")
    if "🟡" in memo_md[:800] or "pivot" in head:
        return ("pivot", "🟡 PIVOT")
    if "🔴" in memo_md[:800] or "pass" in head:
        return ("pass", "🔴 PASS")
    return None


def verdict_pill(memo_md: str) -> None:
    v = detect_verdict(memo_md)
    if not v:
        return
    css_class, label = v
    st.markdown(
        f'<div class="verdict {css_class}">{label}</div>',
        unsafe_allow_html=True,
    )
