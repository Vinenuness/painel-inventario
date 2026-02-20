# ================================
# SERVER.PY
# ================================
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timezone
import sqlite3
import json
import os
import uuid
import re

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_DIR, "db.sqlite3")

AGENT_TOKEN = "SEU_TOKEN_SUPER_SECRETO"

app = Flask(__name__, template_folder=os.path.join(APP_DIR, "templates"))


# ================================
# HELPERS
# ================================
def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def norm_tag(tag: str) -> str:
    tag = (tag or "").strip().upper().replace(" ", "")
    if tag and not tag.startswith("EVO"):
        tag = f"EVO-{tag}"
    if tag.startswith("EVO") and "-" not in tag and len(tag) > 3:
        tag = "EVO-" + tag[3:]
    return tag

def is_valid_tag(tag: str) -> bool:
    return bool(re.fullmatch(r"EVO-\w{2,20}", tag or ""))


# ================================
# DATABASE INIT
# ================================
def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS computers (
                agent_id TEXT PRIMARY KEY,
                device_uid TEXT,
                hostname TEXT,
                alias TEXT,
                tag_evo TEXT,
                last_seen TEXT,
                payload_json TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS scripts (
                script_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                job_id TEXT PRIMARY KEY,
                device_uid TEXT NOT NULL,
                script_id TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT,
                started_at TEXT,
                finished_at TEXT,
                stdout TEXT,
                stderr TEXT,
                exit_code INTEGER
            )
        """)
        conn.commit()

init_db()