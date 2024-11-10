from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from collections import Counter
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/api/fetch-top-words", methods=["POST"])
def fetch_top_words():
    data = request.json
    url = data.get("url")
    top_n = int(data.get("topN"))

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text().lower()

    # Extract words and calculate frequency
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words).most_common(top_n)

    return jsonify({"topWords": [{"word": word, "frequency": count} for word, count in word_counts]})

if __name__ == "__main__":
    app.run(port=5000)
