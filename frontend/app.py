from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Call backend API
    resp = requests.get('http://backend:5000/api/message')
    message = resp.json().get('message', 'No message')
    return render_template_string("<h1>Frontend says: {{ msg }}</h1>", msg=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
