import matplotlib.pyplot as plt
import numpy as np


def plot(distribution):
    '''
    Функция построения графика
    '''
    x = np.arange(0, len(distribution)/10, 0.1)
    y = distribution
    figure, axis = plt.subplots()
    axis.bar(x, y)
    figure.set_figwidth(10)    #  ширина
    figure.set_figheight(6)    #  высота
    plt.xlabel('Расстояние')
    plt.title(r'Гистограмма распределения расстояний')
    plt.show()




