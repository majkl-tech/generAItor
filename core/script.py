import os
import json

from groq import Groq


def vytvor_scenar(tema: str) -> dict:
    """Zavolá Groq a vrátí scénář videa jako slovník (parsovaný JSON)."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    odpoved = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "Jsi scenárista krátkých videí o statistikách v Evropě. "
                    "Odpovídej POUZE validním JSON v tomto tvaru: "
                    '{"title": str, "scenes": [{"text": str, "duration": number}]}'
                ),
            },
            {"role": "user", "content": f"Vytvoř scénář o tématu: {tema}"},
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
    )
    return json.loads(odpoved.choices[0].message.content)
