import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

from app.prompts.review_prompt import build_review_prompt


BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def gen_review(code: str):

    prompt = build_review_prompt(code)

    response = model.generate_content(
        prompt,
        stream=True
    )

    for chunk in response:
        text = getattr(chunk, "text", None)

        if text:
            yield text

def gen_project_review(files):

    for file in files:

        yield "\n"
        yield "=" * 60 + "\n"
        yield f"Reviewing: {file.path}\n"
        yield "=" * 60 + "\n\n"

        yield from gen_review(file.content)

        yield "\n\n"