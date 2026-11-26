import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    vertexai=True,
    project="privacy-agent-508213",
    location="global"
)

response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=["What is AI?", ]
)

for chunk in response:
    print(chunk.text, end="")
