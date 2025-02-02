from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Function to send request to the API and get the rewritten title
def get_rewritten_title(title, tone):
    url = "https://text-tad.droplinked.workers.dev/"
    headers = {
        "Content-Type": "application/json",
        "api-key": "A9d$7Gm@4LpXzQ!2TbVc"
    }
    payload = {
        "command_name": "title",
        "title": title,
        "tone": tone
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        print("API Response:", result)  # Debugging information
        if "output" in result:
            return result["output"]
        else:
            print("Error: 'output' key not found in response")
            print("Full Response:", result)  # Additional debugging information
            return "Error: No title returned"
    else:
        print("API Request Failed:", response.status_code, response.text)  # Debugging information
        return "Error: API request failed"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rewrite_title', methods=['POST'])
def rewrite_title():
    data = request.json
    title = data.get('title')
    tone = data.get('tone')
    rewritten_title = get_rewritten_title(title, tone)
    return jsonify({'rewritten_title': rewritten_title})

if __name__ == '__main__':
    app.run(debug=True)