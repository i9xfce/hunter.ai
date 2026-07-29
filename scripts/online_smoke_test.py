#!/usr/bin/env python3
"""Smoke test a running JobHunter AI backend over HTTP."""
from __future__ import annotations

import json
import sys
import urllib.request

BASE_URL = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:8000"

def request(path: str, payload: dict | None = None) -> dict:
    data = None if payload is None else json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"} if payload is not None else {}
    with urllib.request.urlopen(urllib.request.Request(f"{BASE_URL}{path}", data=data, headers=headers), timeout=10) as response:
        return json.loads(response.read().decode())

health = request("/health")
match = request("/api/v1/jobs/match", {
    "job": {
        "title": "Cloud Engineer",
        "company": "Acme",
        "source_url": "https://example.com/jobs/cloud-engineer",
        "description": "Cloud role",
        "skills": ["Python", "AWS", "Terraform"],
    },
    "profile_skills": ["Python", "AWS", "Docker"],
})

assert health["status"] == "ok", health
assert match["score"] == 66, match
assert match["strengths"] == ["aws", "python"], match
assert match["gaps"] == ["terraform"], match
print(json.dumps({"health": health, "match": match}, indent=2))
