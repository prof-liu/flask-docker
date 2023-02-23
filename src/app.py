import requests
from flask import Flask, jsonify, request, render_template_string, render_template

app = Flask(__name__)


@app.route("/universities")
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())

@app.route('/')
def home():  # put application's code here
    return render_template('home.html') 

@app.route('/hello')
def hello():  # put application's code here
    return render_template_string('Hello World!') #'Hello World!'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
