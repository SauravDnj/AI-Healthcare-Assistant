"""
openai_client.py
────────────────
Handles all communication with the Groq API using built-in urllib.
No extra library needed — works out of the box!
"""

import urllib.request
import urllib.error
import json

# ── Groq API Key ──────────────────────────────────────────────────────────────
API_KEY = "gsk_YOUR_API_KEY_HERE"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL    = "llama-3.3-70b-versatile"
# ─────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are HealthAI, a knowledgeable and empathetic AI Healthcare Assistant 
designed for educational purposes. Your role is to:

1. Provide clear, accurate general health information
2. Explain medical terms in simple language
3. Offer wellness, nutrition, and lifestyle tips
4. Help users understand symptoms (without diagnosing)
5. Encourage users to consult real doctors for personal medical issues

Guidelines:
- Always be warm, supportive, and easy to understand
- Use bullet points and structured responses when helpful
- Always remind users to see a doctor for serious or personal concerns
- Never diagnose, prescribe, or replace professional medical advice
- Keep responses concise but informative (aim for 150-250 words)

You are a college project demo assistant focused on Healthcare AI."""


def get_ai_response(chat_history: list) -> str:
    """
    Send the conversation history to Groq and return the assistant's reply.
    Uses only Python's built-in urllib — no extra packages required.
    """
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + chat_history

        payload = json.dumps({
            "model": MODEL,
            "messages": messages,
            "max_tokens": 400,
            "temperature": 0.7,
        }).encode("utf-8")

        req = urllib.request.Request(
            GROQ_URL,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}",
                "User-Agent": "Mozilla/5.0",
            },
            method="POST"
        )

        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"].strip()

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        err  = body.lower()
        if e.code == 401 or "invalid api key" in err or "auth" in err:
            return "❌ API Key Error: Your Groq API key is invalid. Please check openai_client.py."
        elif e.code == 429 or "rate" in err:
            return "⚠️ Rate limit reached. Please wait a moment and try again."
        else:
            return f"❌ HTTP Error {e.code}: {body[:200]}"

    except urllib.error.URLError as e:
        return "🌐 Connection error. Please check your internet connection."

    except Exception as e:

        return f"❌ Unexpected error: {str(e)}"
