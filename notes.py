import csv

with open('HR_comma_sep.csv', 'rb') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# point = data[0]
# print point['salary']

# split raw data into training and test data: 70% and 30% respectively
def separate_data(raw):
    train_data = raw[0:7499]
    test_data = raw[7499:]
    return train_data, test_data

separate_data(data)

#DONE: Sort through data
#DONE: Github project
#DONE: Separate the data into train and test sets
#DONE: Write a classifier to determine whether or not a person will leave given some points
#TODO: Write a front end that's pretty and easy to display
#TASK: Given an employee, will they leave the company?
