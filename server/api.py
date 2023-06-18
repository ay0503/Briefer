from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/summarize', methods=['GET'])
def summarize():
    # text = request.json['text']

    # Here you would typically call a function to summarize the text.
    # For simplicity, we'll just return the first 100 characters.
    summary = "text"

    return jsonify(summary=summary)

if __name__ == '__main__':
    app.run(port=3000)
