import os
from random import choices
import openai

with open('key.txt') as key:
    api_key = key.read()

with open('input.txt') as input:
    prom = input.read()

openai.api_key = (api_key)

response = openai.Completion.create(
  model="davinci",
  prompt=prom,
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

if __name__ == '__main__':  
    print(response['choices'][0])