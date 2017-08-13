# performs stochastic gradient descent on dataset
from math import exp
import random

# DONE: Calculate logistic
def logistic(x):
    return 1 / (1 + exp(-x))

# DONE: Calculate dot product of two lists
def dot(x, y):
    s = 0
    for i in range(len(x)):
        s += (x[i] * y[i])
    return s

# DONE: Calculate prediction based on model
def predict(model, point):
    features = point['features']
    x = dot(features, model)
    return logistic(x)

# DONE: Calculate accuracy of predictions on data
def accuracy(data, predictions):
    correct = 0

    for i in range(len(data)):
        if predictions[i] > 0.5:
            pred = True
        else:
            pred = False
        if data[i]['label'] == pred:
            correct += 1

    return float(correct)/len(data)

# TODO: Update model using learning rate and L2 regularization
def update(model, point, delta, rate, lam):
    # the model is the weight vector that I need to update
    # loop through every weight in the model vector
    # and update the weight

    # randomly select a point and run the model on it (this is already selected for us!)
    prediction = predict(model, point) #logistic(dot(model, point['features']))
    # calculate the loss
    # loss = ((prediction - point['label'])**2) +  (lam * )
    # calculate the error of that point and adjust model weights based on gradient of error
    for i in range(len(model)):
        wi = model[i]
        gradient = ((-1 * lam) * wi) + (point['features'][i] * (point['label'] - prediction))

        model[i] = wi + (gradient*rate)
    # pass

def initialize_model(k):
    return [random.gauss(0, 1) for x in range(k)]

# TODO: Train model using training data
def train(data, epochs, rate, lam):
    model = initialize_model(len(data[0]['features']))
    for e in range(epochs):
        for x in range(len(data)): # run through N times (where N is the number of items in our data)
            # pick a random point in the data
            point = random.choice(data)
            # print point
            update(model, point, 0, rate, lam)
            # print model


    return model

def extract_features(raw):
    data = []
    for r in raw:
        point = {}
        point['label'] = (r['left'] == '1')

        features = []
        features.append(1.) # I think this is the weight??
        features.append(r['satisfaction_level'])
        features.append(float(r['last_evaluation']) > 0.5)
        # features.append(float(r['age'])/100)
        # features.append(float(r['education_num'])/20)
        # features.append(r['marital'] == 'Married-civ-spouse')
        #TODO: Add more feature extraction rules here!
        # features.append(r['type_employer'] == 'Never-worked')
        # features.append(r['type_employer'] == 'Without-pay')
        # features.append(r['relationship'] == 'Own-child')
        # features.append(float(r['hr_per_week'])/80)
        # features.append(r['occupation'] == 'Exec-managerial' or
        #                 r['occupation'] == 'Prof-specialty' or
        #                 r['occupation'] == 'Adm-clerical' or
        #                 r['occupation'] == 'Sales' or
        #                 r['occupation'] == 'Tech-support' or
        #                 r['occupation'] == 'Armed-Forces')
        # features.append(r['capital_gain'] > 3000)
        # features.append(r['capital_loss'] > 0)
        point['features'] = features
        data.append(point)
    return data

# TODO: Tune your parameters for final submission
def submission(data):
    return train(data, 5, .01, 0)
