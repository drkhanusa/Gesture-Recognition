import csv
import numpy as np
from PIL import Image as im
def read_csv():
    with open('D:/Afor_Giatoc/data/20211216_JAN_G_H/10/12.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    a = int(len(l))-1
    Acc_x = np.zeros((a, a), dtype=float)
    Acc_y = np.zeros((a, a), dtype=float)
    Acc_z = np.zeros((a, a), dtype=float)
    for i in range(a):
        Acc_x[i, 0] = l[i + 1][1]
        Acc_x[0, i] = l[i + 1][1]
        Acc_y[i, 0] = l[i + 1][2]
        Acc_y[0, i] = l[i + 1][2]
        Acc_z[i, 0] = l[i + 1][3]
        Acc_z[0, i] = l[i + 1][3]
    for i in range(Acc_x.shape[0]):
        for j in range(Acc_x.shape[1]):
            Acc_x[i, j] = abs(Acc_x[i, 0] - Acc_x[0, j])
            Acc_y[i, j] = abs(Acc_y[i, 0] - Acc_y[0, j])
            Acc_z[i, j] = abs(Acc_z[i, 0] - Acc_z[0, j])
    # data_x = im.fromarray(Acc_x)
    # data_y = im.fromarray(Acc_y)
    # data_z = im.fromarray(Acc_z)
    # data_x.show()
    # data_y.show()
    # data_z.show()
    img = np.zeros([a, a, 3])
    img[:, :, 0] = Acc_x
    img[:, :, 1] = Acc_y
    img[:, :, 2] = Acc_z

    image = im.fromarray(img.astype(np.uint8))
    image.save('12.png')
    # image.show(

read_csv()

