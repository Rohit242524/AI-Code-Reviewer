import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

from app.prompts.review_prompt import REVIEW_PROMPT

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def gen_review(code: str):

    prompt = REVIEW_PROMPT.format(code=code)

    response = model.generate_content(prompt)

    return response.text