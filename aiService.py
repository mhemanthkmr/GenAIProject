from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from utils import extractJSON

def call_llm(user_prompt, system_prompt):
    client = genai.Client(
        api_key=os.getenv('GOOGLE_API_KEY'),
    )
    model = "gemini-flash-latest"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        system_instruction=[
            types.Part.from_text(text=system_prompt),
        ],
    )
    response =  client.models.generate_content(
        model = model,
        contents = contents,
        config = generate_content_config
    )
    return extractJSON(response.text)