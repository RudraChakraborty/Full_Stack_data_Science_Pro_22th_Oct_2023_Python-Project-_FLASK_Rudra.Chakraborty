from flask import Flask, render_template
import requests
app = Flask(__name__)
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()[:5]
@app.route("/")
def home():
    api_data = fetch_data()
    return render_template("api.html", data=api_data)
if __name__ == "__main__":
    app.run(debug=True)
