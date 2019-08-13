import sys
import calendar
import csv
import datetime
from pprint import pprint
import re
from statistics import mean, stdev


def dates_dictionary(file):

    date = {}

    with open(file) as f:
        reader = csv.reader(f)

        count = 0
        for row in reader:
            if count == 0:
                count += 1
            else:
                if row[1] not in date.keys():
                    date[row[1]] = list()
                    date[row[1]].append(float(row[2]))
                else:
                    date[row[1]].append(float(row[2]))

    return date


def stockName(filePath):
    stock_name = []
    with open(filePath) as f:
        try:
            line_count = 0
            csv_reader = csv.reader(f)

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    stock_name.append(row[0])
                    line_count += 1

            print(list(set(stock_name)))

            return list(set(stock_name))
        except FileNotFoundError:
            print("Enter the Correct File Path")


# def inputDate():
#     try:
#
#         start_date = input('\"From which date you want to start [Format(DD-MMM-YYY)]\":-   ')
#         end_date = input('\"Till which date you want to analyze [Format(DD-MMM-YYY)]\":-   ')
#
#         sd, sm, sy = start_date.split("-")
#         ed, em, ey = end_date.split("-")
#
#         sdd = datetime.datetime(sy, sm, sd)
#         edd = datetime.datetime(ey, em, ed)
#
#         if sdd == edd or sdd > edd:
#             inputDate()
#         else:
#             return sdd, edd
#
#     except Exception:
#         print("Enter date in this format (DD-MM-YYYY)")
#         inputDate()


if __name__ == '__main__':
    file = sys.argv[1]
    unique_stock_name = stockName(file)

    stock = input('\"Welcome Agent! Which stock you need to process?\":-   ')
    stock_price = list()
    calendar_di = dict((k, v) for k, v in enumerate(calendar.month_abbr))

    if stock in unique_stock_name:
        start_date = input('\"From which date you want to start [Format(DD-MMM-YYY)]\":-   ')
        end_date = input('\"Till which date you want to analyze [Format(DD-MMM-YYY)]\":-   ')

        # start_date = '20-Jan-2019'
        # end_date = '30-Jan-2019'

        # sd, sm, sy = start_date.split("-")
        # ed, em, ey = end_date.split("-")
        #
        # sdd = datetime.datetime(int(sy), calendar_di[sm]), int(sd))
        # edd = datetime.datetime(int(ey), calendar_di[em], int(ed))

        with open(file) as f:
            reader = csv.reader(f)

            col = 0
            for row in reader:
                if col == 0:
                    col += 1
                # Date Comparision
                else:
                    if start_date <= row[2] or end_date >= row[2]:
                        stock_price.append(float(row[2]))
                        col += 1

                    # d, m, y = row[1].split("-")
                    # data_date = datetime.datetime(int(y), calendar_di[m], int(d))

                    # if sdd <= data_date or edd >= data_date:
                    #     stock_price.append(float(row[2]))
                    #     col += 1
    else:

        r = re.compile(stock)
        search_list = list(filter(r.match, unique_stock_name))

        for x in search_list:

            entry = input('\"Oops! Do you mean {}? y or n\":-'.format(stock))

            if entry.lower() == 'y':
                start_date = input('\"From which date you want to start\":-   ')
                end_date = input('\"Till which date you want to analyze\":-   ')

                with open(sys.argv[1]) as f:
                    reader = csv.reader(f)

                    col = 0
                    for row in reader:
                        if col == 0:
                            col += 1
                        if start_date == row[1] or end_date == row[1]:
                            # stock_price.update({row[1]: row[2]})
                            stock_price.append(float(row[2]))
            else:
                pass


    if len(stock_price) > 1:
        mean_value = mean(stock_price)
        std_deviation = stdev(stock_price)
    else:
        mean_value = 0
        std_deviation = 0

    # Buy Date
    # Sell Date

    if len(stock_price) > 0:
        maximum = max(stock_price)
        minimum = min(stock_price)
    else:
        maximum = 0
        minimum = 0

    #############################################################
    data = dates_dictionary(file)
    # print(data)

    maximum = 0
    datetosell = ''
    for key, value in data.items():
        if maximum > min(value):
            pass
        else:
            maximum = min(value)
            datetosell = key


    # Date to buy
    minimum = 0
    datetobuy = ''
    new_di = {}

    for key, value in data.items():
        new_di[key] = min(value)

    for key, value in new_di.items():
        if minimum == 0:
            minimum = value
            datetobuy = key
        elif minimum > value:
            minimum = value
            datetobuy = key

    ########################################################
    print("Here is the result:-")
    print("Mean:- {}".format(mean_value))
    print("Std:- {}".format(std_deviation))
    print("Buy date: {}".format(datetobuy))
    print("Sell date: {}".format(datetosell))
    print("Profit: Rs. {}".format(maximum - minimum))

