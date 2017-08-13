import data_parsing
from sgd import extract_features
import csv

with open('HR_comma_sep.csv', 'rb') as f:
    reader = csv.DictReader(f)
    data = list(reader)

train_data = data[0:10500]
test_data = data[10500:]

print data[0]['left']

print extract_features(train_data)
print extract_features(test_data)
