from sgd import extract_features
from sgd import logistic, dot, predict, accuracy, submission, extract_features
import csv
import random

from test import test_submission, return_train_data, return_test_data

test_submission()

def predict():
    train_data = return_train_data()
    test_data = return_test_data()
    model = submission(train_data)

    print test_data[0]
    # predictions = [predict(model, p) for p in train_data]

predict()
