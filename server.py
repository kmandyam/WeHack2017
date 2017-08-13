# from bs4 import BeautifulSoup
import urllib
import csv
from flask import Flask
from flask import request
from flask_cors import CORS
import json
from test import test_submission

import os, sys, csv, urllib

app = Flask(__name__)
CORS(app)

@app.route("/loaddata" , methods=['GET', 'POST'])

def load_trained_data():
    # urlList = request.form['urlArray']

    # urlList = json.loads(urlList)
    # print urlList, "FIRST ONE"

    # print "HELLO WORLD", len(urlList)
    train_accuracy, test_accuracy = test_submission()
    return "Training Accuracy: " + str(train_accuracy) + ", Testing Accuracy: " + str(test_accuracy)


app.run()
