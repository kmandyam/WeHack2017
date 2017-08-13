from sgd import extract_features
from sgd import logistic, dot, predict, accuracy, submission, extract_features
import csv
import random

with open('HR_comma_sep.csv', 'rb') as f:
    reader = csv.DictReader(f)
    data = list(reader)

random.shuffle(data)

train_separate = data[0:10500]
test_separate = data[10500:]


train_data = extract_features(train_separate)
test_data = extract_features(test_separate)



def test_logistic():
    self.assertAlmostEqual(logistic(1),  0.7310585786300049)
    self.assertAlmostEqual(logistic(2),  0.8807970779778823)
    self.assertAlmostEqual(logistic(-1),  0.2689414213699951)

def test_dot():
    d = dot([1.1,2,3.5], [-1,0.1,.08])
    self.assertAlmostEqual(d, -.62)

def test_predict():
    model = [1,2,1,0,1]
    point = {'features':[.4,1,3,.01,.1], 'label': 1}
    p = predict(model, point)
    self.assertAlmostEqual(p, 0.995929862284)

def test_accuracy():
    data = train_data
    a = accuracy(data, [0]*len(data))
#     self.assertAlmostEqual(a, 0.751077514754)

def test_submission():
    valid_data = test_data
    model = submission(train_data)
    predictions = [predict(model, p) for p in train_data]
    print
    print
    # print predictions
    train_accuracy = accuracy(train_data, predictions)
    print "Training Accuracy:", train_accuracy
    # print train_data
    predictions = [predict(model, p) for p in valid_data]
    valid_accuracy = accuracy(valid_data, predictions)
    print "Validation Accuracy:", valid_accuracy
    print
    return train_accuracy, valid_accuracy

test_submission()
