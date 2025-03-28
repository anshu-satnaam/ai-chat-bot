from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__, template_folder='templates')

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")  # Use environment variable
)

@app.route("/", methods=["GET", "POST"])
def index():
    # ... (keep your existing index route logic)
    return render_template("index.html", response_text=response_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)