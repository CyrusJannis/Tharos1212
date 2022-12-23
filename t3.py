import os
import openai

openai.api_key = "REDACTED_OPENAI_KEY"
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