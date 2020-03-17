import pickle
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://trouver-f8d97.firebaseio.com/', None)

check = False

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

def sendData():
    data =  { 'Name': 'John Doe',
          'RollNo': 3,
          'Percentage': 70.02
          }
    result = firebase.post('/trouver-f8d97/',data)
    
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        result = load_model(url)
        check = True
        return render_template("result.html", result=result)

if check is True:
    sendData()

if __name__ == '__main__':
    print("Starting Server...")
    print("Model Loaded...")
    app.run(port=5000, debug=True)
