import numpy as np


class CalculateNumpy:
    vmin = None
    vmax = None
    list_of_length = np.array([])

    def calcul_length(self, a: list, b: list):
        square = np.square(a - b)
        return np.sum(square)
    
    def set_min_max(self, a, b, length):
        args = (a, b, length)
        if not self.vmax:
            self.vmax = args
        else:
            self.vmax = args if length > self.vmax[2] else self.vmax

        if not self.vmin:
            self.vmin = args
        else:
            self.vmin = args if length < self.vmin[2] else self.vmin


    def __init__(self, data: list):
        len_data = len(data) - 1
        for a in range(len_data, 0, -1):
            for b in range(len_data, 0, -1):
                if a != b:
                    continue
                square = np.square(data[a] - data[b])
                length = np.sum(square)
                np.append(self.list_of_length, length)
                self.set_min_max(a, b, length)
            len_data -= 1
            data = np.delete(data, a, axis=0)
        print(self.vmax)
        print(self.vmin)
