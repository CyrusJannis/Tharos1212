import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="A man standing on a cliff",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)