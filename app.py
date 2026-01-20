# app.py
# Simple Python client for AI Gateway (Ollama)

import os
import sys
import json
import requests

GATEWAY_URL = os.getenv("GATEWAY_URL", "http://localhost:8000/v1/chat/completions")
API_KEY = os.getenv("API_KEY", "dev-key-123")  # match your .env / gateway config


def run_chat(prompt: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt or "Review this function",
            }
        ]
    }

    try:
        resp = requests.post(GATEWAY_URL, headers=headers, data=json.dumps(payload))
        if resp.status_code != 200:
            print("Gateway error:", resp.status_code, resp.text)
            sys.exit(1)

        data = resp.json()
        print("Gateway response:")
        print(json.dumps(data, indent=2))
    except Exception as e:
        print("Request failed:", e)


if __name__ == "__main__":
    user_prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    run_chat(user_prompt)
