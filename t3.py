import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
prompt = input("Enter prompt\n> ")

response = openai.Completion.create(
  model="code-davinci-003",
  prompt="",
  temperature=0,
  max_tokens=600000,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response["choices"][0]["text"])