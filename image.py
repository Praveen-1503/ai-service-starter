import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    enterprise=True,
    project="privacy-agent-508213",
    location="global"
)

with open("face.jpg", "rb") as f:
    image_bytes = f.read()

media = genai.types.Part.from_bytes(
    data = image_bytes,
    mime_type="image/jpg",
)

response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=["How many people are there in the image? ", media],
    config={
        "thinking_config" : {
            "include_thoughts":True
        }
    }
)

for chunk in response:
    for part in chunk.candidates[0].content.parts:
        if part.thought:
            print("thinking")
        else:
            print(part.text, flush=True, end="")
