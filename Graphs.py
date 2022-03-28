import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
def read_csv():
    Times = []
    Acc_x = []
    Acc_y = []
    Acc_z = []
    plt.style.use('seaborn')
    data = pd.read_csv('20210419_195115.csv', delimiter=',')
    for i in range(len(data['Time'])):
        if (data['Time'][i] == -1):
            plt.plot(Times, Acc_x, color='red', label='Acc_x')
            plt.plot(Times, Acc_y, color='green', label='Acc_y')
            plt.plot(Times, Acc_z, color='blue', label='Acc_z')
            plt.legend()
            plt.xlabel("Times")
            plt.grid(True)
            plt.show()
            Times.clear()
            Acc_x.clear()
            Acc_y.clear()
            Acc_z.clear()
        elif (data['Time'][i] == 0):
            pass
        else:
            Times.append(data['Time'][i])
            Acc_x.append(data['Ax'][i])
            Acc_y.append(data['Ay'][i])
            Acc_z.append(data['Az'][i])
