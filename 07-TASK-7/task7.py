from flask import Flask, render_template
import requests

app = Flask(__name__)

API = "sa9ZXkeMdcfJbio79goYaI8dgf1zdHDQpz0yktKo"
URL = f"https://api.nasa.gov/planetary/apod?api_key={API}&date=2024-10-04"

@app.route('/', methods=['GET'])
def index():
    response = requests.get(URL)
    data = response.json()
    return render_template('index.html', apod_data=data)


@app.route('/display', methods=['GET'])
def display():
    return ['Hamza', 'Ali']

if __name__ == '__main__':
    app.run(debug=True)