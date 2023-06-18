import openai
import os

openai.api_key = openai.api_key = os.environ["OPENAI_API_KEY"]
inputData = "https://www.cnn.com/travel/article/luggage-trackers-airtags-missing-bags/index.html" 

MODEL = "gpt-4"
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": f'In 3 bullet points please summarize the content in this: {inputData}'},
    ],
    temperature=0,
)

print(response)
