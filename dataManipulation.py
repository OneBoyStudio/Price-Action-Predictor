import csv
import math
import manipulationFunctions

input_data = []

with open('PLTR.csv') as file: #change 'PLTR.csv' to whatever csv file for stock information you utilize
    csv_reader = csv.reader(file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            input_data.append([row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])])

parse_one = manipulationFunctions.firstParse(input_data)

m_vals = manipulationFunctions.calculateSlopeAndRValues(parse_one)[0]
r_vals = manipulationFunctions.calculateSlopeAndRValues(parse_one)[1]

rsi_vals = manipulationFunctions.calculateRSIandATR(parse_one, input_data)[0]
atrs = manipulationFunctions.calculateRSIandATR(parse_one, input_data)[1]

final_data = manipulationFunctions.appendIncrDecr(input_data, manipulationFunctions.createFinalData(rsi_vals, parse_one, r_vals, m_vals, atrs))

print(final_data)

with open('dataManipulatedPLTR.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(final_data)