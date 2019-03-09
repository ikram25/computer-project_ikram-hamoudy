def funa(x, Y, dY):
    xY_avg = 0
    sum_dY = 0
    for i in range(0, len(x)):
        xY_avg = xY_avg + x[i] * Y[i] / dY[i] ** 2
        sum_dY = sum_dY + 1 / dY[i] ** 2
    xY_avg = xY_avg / sum_dY
    x_avg = 0
    x_avg_sq = 0
    for i in range(0, len(x)):
        x_avg = x_avg + x[i] / dY[i] ** 2
        x_avg_sq = x_avg_sq + x[i] ** 2 / dY[i] ** 2
    x_avg = x_avg / sum_dY
    x_avg_sq = x_avg_sq / sum_dY
    Y_avg = 0
    for i in range(0, len(Y)):
        Y_avg = Y_avg + Y[i] / dY[i] ** 2
    Y_avg = Y_avg / sum_dY

    return (xY_avg - x_avg * Y_avg) / (x_avg_sq - x_avg ** 2)


def funda(x, dY):
    dY_avg_sq = 0
    sum_dY = 0
    sum1 = 0
    for i in range(0, len(dY)):
        dY_avg_sq = dY_avg_sq + dY[i] ** 2 / dY[i] ** 2
        sum_dY = sum_dY + 1 / dY[i] ** 2
        sum1 = sum1 + 1
    dY_avg_sq = dY_avg_sq / sum_dY
    x_avg = 0
    x_avg_sq = 0
    for i in range(0, len(x)):
        x_avg = x_avg + x[i] / dY[i] ** 2
        x_avg_power = x_avg_sq + x[i] ** 2 / dY[i] ** 2
    x_avg = x_avg / sum_dY
    x_avg_sq = x_avg_sq / sum_dY

    return (dY_avg_sq / (count * (x_avg_sq - x_avg ** 2))) ** 0.5


def funb(Y,a,x,dY,):
    sum_dY = 0
    Y_avg = 0
    for i in range(0, len(Y)):
        Y_avg = Y_avg + Y[i] / dY[i] ** 2
        sum_dY = sum_dY + 1 / dY[i] ** 2
    Y_avg = Y_avg / sum_dY
    x_avg = 0
    for i in range(0, len(x)):
        x_avg = x_avg + x[i] / dY[i] ** 2
    x_avg = x_avg / sum_dY

    return Y_avg - a * x_avg


def fundb(x, dY):
    dY_avg_sq = 0
    sum_dY = 0
    sum1 = 0
    for i in range(0, len(dY)):
        dY_avg_sq = dY_avg_sq + dY[i] ** 2 / dY[i] ** 2
        sum_dY = sum_dY + 1 / dY[i] ** 2
        sum1 = sum1 + 1
    dY_avg_sq = dY_avg_sq / sum_dY
    x_avg = 0
    x_avg_sq = 0
    for i in range(0, len(x)):
        x_avg = x_avg + x[i] / dY[i] ** 2
        x_avg_sq = x_avg_sq + x[i] ** 2 / dY[i] ** 2
    x_avg = x_avg / sum_dY
    x_avg_sq = x_avg_sq / sum_dY

    return (dY_avg_sq * x_avg_sq / (count * (x_avg_sq - x_avg** 2))) ** 0.5

def funchi2red(chi, x):
    sum1 = 0
    for i in range(0, len(x)):
        sum1 = sum1 + 1
    return chi / (sum1 - 2)


def funchi2(Y,a,b,x,dY):
    Chi2 = 0
    for i in range(0, len(x)):
        Chi2 = Chi2 + ((Y[i] - (a * x[i] + b)) / dY[i]) ** 2
    return Chi2


def check_rows(data):
    for x in data:
        if not ('axis' or 'axis') in x:
            datalist = x.split(' ')
            a = datalist[0].lower()
            datalist.pop(0)
            if a == 'x':
                x_data = list(map(float, line_data_list))
            elif a == 'Y':
                Y_data = list(map(float, line_data_list))
            elif a == 'dx':
                dx_data = list(map(float, line_data_list))
            elif a == 'dY':
                dY_data = list(map(float, line_data_list))

    if len(x_data) != len(Y_data) and len(x_data) != len(dY_data) \
        and len(x_data) != len(dx_data) and len(Y_data) != len(dx_data) \
        and len(Y_data) != len(dY_data) and len(dY_data) \
        != len(dx_data):
        print ('Input file error: Data lists are not the same length')
        exit()
    for i in dx_data:
        if i <= 0:
            print ('Input file error: Not all uncertainties are positive.')
            exit()
    for i in dY_data:
        if i <= 0:
            print ('Input file error: Not all uncertainties are positive.')
            exit()
    return (x_data, Y_data, dx_data, dY_data)


def check_column(data):
    cheked = []

    for i in data[:len(data) - 4]:
        a = i.strip('\n').lower().split()
        cheked.append(a)
    column = len(cheked[0])
    length = len(cheked)
    my_data = []
    for t in range(column):
        list1 = []
        for i in range(length):
            try:
                list1.append(cheked[i][t])
            except Exception as e:
                pass
        my_data.append(list1)

    for item in my_data:
        b = item[0]
        if b == 'x':
            x = list(map(float, item[1:]))
        elif b == 'Y':
            Y = list(map(float, item[1:]))
        elif b == 'dx':
            Dx = list(map(float, item[1:]))
        elif b == 'dY':
            dY = list(map(float, item[1:]))

    if len(x) != len(Y) and len(x) != len(dY) or len(x) != len(Dx) and len(Y) != len(Dx) or len(Y) != len(dY) and len(dY) != len(Dx):
        print ('Input file error: Data lists are not the same length')
        exit()
    for k in Dx:
        if k <= 0:
            print ('Input file error: Not all uncertainties are positive.')
            exit()
    for k in dY:
        if k <= 0:
            print ('Input file error: Not all uncertainties are positive.')
            exit()
    
    return (x, Y, Dx, dY)


import matplotlib.pyplot as plt
import numpy as np


def fit_linear(filename):
    my_file = open(filename)
    data = my_file.read()
    data = data.split('\n')

    mydata = data[0]
    datalist = mydata.split(' ')
    sum1 = len(datalist)

    for z in data:
        if 'x axis' in z:
            xlabel = z.split(":")[1]
        if 'y axis' in z:
            ylabel = z.split(":")[1]

    if sum1 == 4:
        (x, Y, Dx, dY) = check_column(data)
        a = funa(x, Y, dY)
        b = funb(Y, a, x, dY)
        chi = funchi2(Y, a, b, x, dY)
        print ('a=', funa(x, Y, dY), '+-', funda(x, dY))
        print ('b=', funb(Y, a, x, dY), '+-', fundb(x, dY))
        print ('chi2=', funchi2(Y, a, b, x, dY))
        print ('chi2_reduced=', funchi2red(chi, x))
        xx = np.array(x)
        YY = np.array(Y)
        lin = a * xx + b
        xarray = np.array(Dx)
        Yarray = np.array(dY)

        y = lin
        plt.errorbar(xx,YY,Yarray,xarray,fmt='none',ecolor='b')
        plt.plot(xx, Y, 'r')
        plt.xlabel(xlabel)
        plt.Ylabel(Ylabel)
        plt.show()
        plt.savefig('linear_fit.svg')
        my_file.close()
    else:

        (x, Y, Dx, dY) = check_rows(data)
        a = funa(x, Y, dY)
        b = funb(Y, a, x, dY)
        chi = funchi2(Y, a, b, x, dY)
        print ('a=', funa(x, Y, dY), '+-', funda(x, dY))
        print ('b=', funb(Y, a, x, dY), '+-', fundb(x, dY))
        print ('chi2=', funchi2(Y, a, b, x, dY))
        print ('chi2_reduced=', funchi2red(chi, x))
        xx = np.array(x)
        YY = np.array(Y)
        lin = a * xx + b
        xarray = np.array(Dx)
        Yarray = np.array(dY)

        y = lin
        plt.errorbar(xx,YY,Yarray,xarray,fmt='none',ecolor='b',)
        plt.plot(xx, Y, 'r')
        plt.xlabel(xlabel)
        plt.Ylabel(Ylabel)
        plt.show()
        plt.savefig('linear_fit.svg')
        my_file.close()
