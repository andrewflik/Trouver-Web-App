# Code by - Devesh Rajput Contact for more info - (deveshrajput978@gmail.com)
import pickle
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json

app = Flask(__name__)


def load_model(url):
    article = Article(url)
    article.download()
    article.parse()
    var = str(article.text)

    model = pickle.load(open('final_model.sav', 'rb'))
    prediction = model.predict([var])
    prob = model.predict_proba([var])
    # truth = prob[0][1]
    return [prediction[0], prob[0][1]]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        result = load_model(url)
        return render_template("result.html", result=result)


if __name__ == '__main__':
    print("Starting Server...")
    print("Model Loaded...")
    app.run(port=5000, debug=True)
