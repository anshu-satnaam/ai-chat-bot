from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Replace with your actual API key
)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None

    if request.method == "POST":
        user_input = request.form.get("user_input")
        image_url = request.form.get("image_url").strip()

        # Prepare message content
        content = [{"type": "text", "text": user_input}]
        if image_url:
            content.append({"type": "image_url", "image_url": {"url": image_url}})

        # Call OpenAI API
        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1-distill-qwen-14b:free",  # Ensure this model supports vision if using images
                messages=[{"role": "user", "content": content}],
                extra_headers={
                    "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
                    "X-Title": "<YOUR_SITE_NAME>",  # Optional
                },
                extra_body={},
            )
            response_text = completion.choices[0].message.content
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render_template("index.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
