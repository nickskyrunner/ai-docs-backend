import openai
import os
from dotenv import load_dotenv
from ai.prompts import build_prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(question: str, docs: str):
    prompt = build_prompt(question, docs)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sei un assistente esperto in documentazione amministrativa."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]