from dotenv import load_dotenv
import os
import openai

load_dotenv()  # take environment variables from .env.

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input("Enter your prompt: ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=100,
  temperature=0
)

print(response["choices"][0]["text"])