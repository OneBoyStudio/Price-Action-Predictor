import csv
import numpy as np
import math
import matplotlib.pyplot as plt

data = []
b_vals = [0, 0, 0, 0, 0, 0, 0]
learning_rate = 0.001
steps = 20000

with open('dataManipulatedPLTR.csv') as file: #dataManipulatedPLTR can be replaced by whatever file you chose to return from dataManipulation.py
    reader = csv.reader(file, delimiter= ',')

    for rows in reader:
        data.append([rows[0], float(rows[1]), float(rows[2]), float(rows[3]), float(rows[4]), float(rows[5]), float(rows[6]), int(rows[7])])

def sigmoid(b, x):

    b0 = b[0]
    b1 = b[1]
    b2 = b[2]
    b3 = b[3]
    b4 = b[4]
    b5 = b[5]
    b6 = b[6]

    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    x6 = x[5]

    exponent = -1*(b0 + (b1*x1) + (b2*x2) + (b3*x3) + (b4*x4) + (b5*x5) + (b6*x6))

    val = 1 / (1 + (math.e**exponent))
    return val

y_vals = []
x_vals = []

for items in data:
    y_vals.append(items[7])
    x_vals.append([items[1], items[2], items[3], items[4], items[5], items[6]])

def cross_entropy_derivative_bias(y, x, b_vals):

    bs = b_vals
    y_vals = y
    x_vals = x

    sum = 0

    for i in range(y_vals.__len__()):
        sum += (sigmoid(bs, x_vals[i]) - y_vals[i])

    return sum

def cross_entropy_derivative_weights(y, x, b_vals, i):

    bs = b_vals
    y_vals = y
    x_vals = x

    xi = i

    sum = 0

    for i in range(y_vals.__len__()):
        sum += (sigmoid(bs, x_vals[i]) - y_vals[i])*x_vals[i][xi]

    return sum

def optimize_vals(i):

    xi = i

    for i in range(steps):

        derivative = cross_entropy_derivative_bias(y_vals, x_vals, b_vals)

        step_size = derivative * learning_rate
        b_vals[0] = b_vals[0] - step_size

        for j in range(xi):

            derivative_ce = cross_entropy_derivative_weights(y_vals, x_vals, b_vals, j)

            step_size = derivative_ce * learning_rate
            b_vals[j+1] = b_vals[j+1] - step_size
    
optimize_vals(6)
print(b_vals)

accuracy = 0

for i in range(x_vals.__len__()):

    sig = sigmoid(b_vals, x_vals[i])

    if (sig > 0.50) and (y_vals[i] == 1):
        accuracy += 1
    elif(sig <= 0.50) and (y_vals[i] == 0):
        accuracy += 1

print(accuracy/x_vals.__len__())

pred_pos = 0
pred_neg = 0
false_pos = 0
false_neg = 0

for i in range(x_vals.__len__()):

    sig = sigmoid(b_vals, x_vals[i])
    print(sig)

    if (sig > 0.5) and (y_vals[i] == 1):
        pred_pos += 1
    elif(sig <= 0.5) and (y_vals[i] == 0):
        pred_neg += 1
    elif(sig > 0.5) and (y_vals[i] == 0):
        false_pos += 1
    elif(sig <= 0.5) and (y_vals[i] == 1):
        false_neg += 1

print(pred_pos)
print(pred_neg)
print(false_pos)
print(false_neg)