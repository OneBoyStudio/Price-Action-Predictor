import math

def firstParse(input_data):

    parse_one = []

    input_num = 0

    for objects in input_data:

        relative_change = (objects[4] - objects[1]) / objects[1]
        relative_range = (objects[2] - objects[3]) / objects[1]

        if input_num < 9:
            parse_one.append([objects[0], relative_change, relative_range])
            input_num += 1
        else:
            past_ten_points = []

            for i in range(10)[::-1]:
                past_ten_points.append(input_data[input_num - i][4])

            parse_one.append([objects[0], relative_change, relative_range, past_ten_points])
            input_num += 1
    
    return parse_one

def calculateSlopeAndRValues(parse_one):

    input_num = 0

    m_vals = []
    r_vals = []

    for regressions in parse_one:

        if input_num < 9:

            input_num += 1
            #the first 9 values wont be in the final input datas
        else:

            n = 0
            x = 0
            y = 0
            x2 = 0 #x^2
            y2 = 0 #y^2
            xy = 0
            for x_value in regressions[3]:
                
                n +=1
                x += x_value
                y += n
                x2 += x_value*x_value
                y2 += n*n
                xy += x_value*n

            m_vals.append(((n*xy) - (x*y))/((n*x2) - x*x))
            r_vals.append(((n*xy) - (x*y))/math.sqrt(((n*x2) - x*x)*((n*y2) - y*y)))
    
    return [m_vals, r_vals]

def calculateRSIandATR(parse_one, input_data):

    input_num = 0

    rsi_vals = []
    atrs = []

    for data in parse_one:

        if input_num < 14:

            pass

        else:

            past_fourteen_points = []

            total_gain = 0
            total_loss = 0

            atr = 0

            for i in range(14):

                if (input_data[input_num - i][4]) > (input_data[input_num - i - 1][4]):

                    total_gain += (input_data[input_num - i][4] - input_data[input_num - i - 1][4])
                
                else:

                    total_loss += (-1* (input_data[input_num - i][4] - input_data[input_num - i - 1][4]))

                if input_num == 14:

                    n1t = input_data[input_num - i][2] - input_data[input_num - i][3]
                    n2t = abs((input_data[input_num - i][2] - input_data[input_num - i - 1][4]))
                    n3t = abs((input_data[input_num - i][3] - input_data[input_num - i - 1][4]))

                    atr += max([n1t, n2t, n3t])
            
            n1 = input_data[input_num][2] - input_data[input_num][3]
            n2 = abs((input_data[input_num][2] - input_data[input_num - 1][4]))
            n3 = abs((input_data[input_num][3] - input_data[input_num - 1][4]))

            tr = max([n1, n2, n3])

            if input_num == 14:
                atr = atr/14

            else:
                atr = ((atrs[input_num - 15] * 13) + tr) / 14

            total_gain = total_gain/14
            total_loss = total_loss/14

            current_gain = (input_data[input_num][4] - input_data[input_num - 1][4])
            current_loss = (-1* (input_data[input_num][4] - input_data[input_num - 1][4]))

            average_gain = ((total_gain*13) + current_gain)/14
            average_loss = ((total_loss*13) + current_loss)/14

            rsi_val = 100 - (100/ (1 + (average_gain/average_loss)))

            rsi_vals.append(rsi_val/100)
            atrs.append(atr/100)
        
        input_num += 1

    return [rsi_vals, atrs]

def createFinalData(rsi_vals, parse_one, r_vals, m_vals, atrs):

    input_num = 0

    final_data = []

    for data in rsi_vals:

        final_data.append([parse_one[input_num][0], parse_one[input_num][1], parse_one[input_num][2], r_vals[input_num], m_vals[input_num], rsi_vals[input_num], atrs[input_num]])
        input_num += 1
    
    return final_data

def appendIncrDecr(input_data, final_data):

    input_num = 0

    finalData = final_data

    for i in range(final_data.__len__() - 1):

        if input_data[i+9][4] > input_data[i+10][4]:
            finalData[i].append(0)
        else:
            finalData[i].append(1)

        input_num += 1

    return finalData