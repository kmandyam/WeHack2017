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
            update(model, point, 0, rate, lam)
            # print model


    return model

def extract_features(raw):
    data = []
    for r in raw:
        point = {}
        point['label'] = (r['left'] == '1')

        features = []
        features.append(float(r['satisfaction_level']) < 0.5)
        features.append(float(r['last_evaluation']) > 0.6 and float(r['last_evaluation']) < 0.8)
        # features.append(float(r['last_evaluation']))
        features.append(float(r['number_project'])/float(r['time_spend_company']))
        features.append(float(r['number_project']) < 2 or float(r['number_project']) > 5)
        features.append(float(r['average_montly_hours']) < 150 or float(r['average_montly_hours']) > 250)
        features.append(float(r['time_spend_company']) > 5)
        features.append(r['salary'] == 'low')

        point['features'] = features
        data.append(point)
    return data

# TODO: Tune your parameters for final submission
def submission(data):
    return train(data, 5, .01, 0)
