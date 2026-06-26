import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

print("ENV_PATH =", ENV_PATH)
print("ENV exists =", ENV_PATH.exists())

load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("GEMINI_API_KEY")

print("API Key =", api_key)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def gen_review(code: str):

    prompt = f"""
You are a Senior Python Code Reviewer.

Review the following Python code.

Python Code:
{code}
"""

    print("Calling Gemini...")

    response = model.generate_content(prompt)

    print("Gemini response received.")

    print(response)

    return response.text