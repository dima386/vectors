import matplotlib.pyplot as plt
from scipy.stats import norm


def plot_graph(data, vmin, vmax):
    x = data
    num_bins = int((abs(vmax[2] - vmin[2]) / 0.1))
    n, bins, patches = plt.hist(x, num_bins, density=False, facecolor='#000000', alpha=0.5)
    y = norm.pdf(bins)
    plt.xlabel('Расстояние')
    plt.title(r'Гистограмма распределения расстояний')
    plt.show()




