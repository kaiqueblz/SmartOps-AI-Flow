import openai
from app.config import OPENAI_KEY

openai.api_key = OPENAI_KEY

def generate_summary(text: str):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Resuma: {text}"}]
    )
    return response.choices[0].message["content"]