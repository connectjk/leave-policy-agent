"""
Deploy agent to Azure AI Foundry via REST API.

Usage (from CI or locally):
  python src/foundry_create_agent.py

Environment variables:
  AZURE_AI_FOUNDRY_ENDPOINT  — Full Foundry project endpoint URL
  AZURE_AI_FOUNDRY_API_KEY   — API key for authentication
"""

import json
import os
import re
import sys
import urllib.request


def sanitize_name(name: str) -> str:
    s = re.sub(r"[^a-z0-9-]", "-", name.lower())
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:63] or "agent"


def deploy():
    endpoint = os.environ.get("AZURE_AI_FOUNDRY_ENDPOINT", "").rstrip("/")
    api_key = os.environ.get("AZURE_AI_FOUNDRY_API_KEY", "")
    if not endpoint:
        print("ERROR: Set AZURE_AI_FOUNDRY_ENDPOINT")
        sys.exit(1)
    if not api_key:
        print("ERROR: Set AZURE_AI_FOUNDRY_API_KEY")
        sys.exit(1)

    url = f"{endpoint}/agents?api-version=2025-05-15-preview"
    payload = json.dumps({
        "name": sanitize_name("Leave-Policy-Agent"),
        "description": """A Leave Policy agent that can search our knowledge base, Provide a Leave Policy related information""",
        "definition": {
            "kind": "prompt",
            "model": "gpt-4o",
            "instructions": """A Leave Policy agent that can search our knowledge base, Provide a Leave Policy related information"""
        }
    }).encode()

    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            print(f"Agent deployed! ID: {data.get('id', 'unknown')}")
            print(f"Name: {data.get('name', '')}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"Deploy failed ({e.code}): {body[:300]}")
        sys.exit(1)


if __name__ == "__main__":
    deploy()
