import data_parsing
from sgd import extract_features
from unittest import TestCase
import unittest
from sgd import logistic, dot, predict, accuracy, submission, extract_features
import csv

with open('HR_comma_sep.csv', 'rb') as f:
    reader = csv.DictReader(f)
    data = list(reader)

train_separate = data[0:10500]
test_separate = data[10500:]

train_data = extract_features(train_separate)
test_data = extract_features(test_separate)


class SGDTest(unittest.TestCase):

    def test_logistic(self):
        self.assertAlmostEqual(logistic(1),  0.7310585786300049)
        self.assertAlmostEqual(logistic(2),  0.8807970779778823)
        self.assertAlmostEqual(logistic(-1),  0.2689414213699951)

    def test_dot(self):
        d = dot([1.1,2,3.5], [-1,0.1,.08])
        self.assertAlmostEqual(d, -.62)

    def test_predict(self):
        model = [1,2,1,0,1]
        point = {'features':[.4,1,3,.01,.1], 'label': 1}
        p = predict(model, point)
        self.assertAlmostEqual(p, 0.995929862284)

    # def test_accuracy(self):
    #     data = train_data
    #     a = accuracy(data, [0]*len(data))
    #     self.assertAlmostEqual(a, 0.751077514754)

    # def test_submission(self):
    #     train_data = extract_features(load_adult_train_data())
    #     valid_data = extract_features(load_adult_valid_data())
    #     model = submission(train_data)
    #     predictions = [predict(model, p) for p in train_data]
    #     print
    #     print
    #     # print predictions
    #     print "Training Accuracy:", accuracy(train_data, predictions)
    #     # print train_data
    #     predictions = [predict(model, p) for p in valid_data]
    #     print "Validation Accuracy:", accuracy(valid_data, predictions)
    #     print


if __name__ == '__main__':
    unittest.main()