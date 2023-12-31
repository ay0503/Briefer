from flask import Flask, request, jsonify
from flask_cors import CORS
import openai, os

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ["OPENAPI_KEY"]

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.json['url']

    MODEL = "gpt-4"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "user",
             "content": f'In 3 bullet points please summarize the content in this: {url}'},
        ],
        temperature=0,
    )

    # print(response.choices[0].message.content)
    return jsonify(summary=response.choices[0].message.content[1:])

if __name__ == '__main__':
    app.run(port=3000)
