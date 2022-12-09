import matplotlib.pyplot as plt
import numpy as np


def pst(data):
    data_pst = []
    temp = True
    for i in range(len(data)):
        if data[i] == 0 and temp == True:
            x = 1
            temp = False
        elif data[i] == 0 and temp == False:
            x = -1
            temp = True
        else:
            x = 0
        data_pst.append(x)

    data_pst.append(0)

    xs = np.repeat(range(len(data_pst)), 2)
    ys = np.repeat(data_pst, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.xlabel(str(data_pst))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, len(data))
    plt.title("Pseudoternary")
    plt.show()
    return data_pst


def inverse_pst(data_pst):
    data = []
    for i in range(len(data_pst)):
        if data_pst[i] == 0:
            data.append(1)
        else:
            data.append(0)
    data = data[:-1]
    return data
