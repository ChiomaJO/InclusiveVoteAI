
from flask import Flask, render_template, request
import json
import re
from pathlib import Path
from difflib import get_close_matches


app = Flask(__name__)

DATA_FILE = Path(__file__).parent / "data" / "electoral_info.json"

def load_electoral_info():
    with open(DATA_FILE, "r",
encoding="utf-8") as file:
        return json.load(file)

    from difflib import get_close_matches

def find_answer(question):
    information = load_electoral_info()

    user_words = set(re.findall(r"\b[a-z0-9]+\b", question.lower()))

    best_match = None
    best_score = 0

    for item in information:
        stored_words = set(re.findall(r"\b[a-z0-9]+\b", item["question"].lower()))

        common_words = user_words.intersection(stored_words)

        score = len(common_words) / len(stored_words)

        if score > best_score:
            best_score = score
            best_match = item

    if best_score >= 0.25:
        return best_match

    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()

    if not question:
        result = None
        message = "Please enter a question before submitting."
    else:
        result = find_answer(question)

        if result is None:
            message = "Sorry, we could not find a verified answer to your question. Please check the official INEC website."
        else:
            message = None

    return render_template(
        "index.html",
        question=question,
        result=result,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
