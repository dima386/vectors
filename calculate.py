from importlib.metadata import distribution
import sys
import numpy as np
from datetime import datetime


class Calculate:
    vmin = None
    vmax = None
    list_of_length = []

    def calcul_length(self, a: list, b: list):
        length = sum(((float(a[i]) - float(b[i])) ** 2 for i, _ in enumerate(a)))
        return length 

    def __init__(self, data: list):
        print(sys.getsizeof(data))
        now = datetime.now()
        len_data = len(data) -1
        for a in range(len_data, 0, -1):
            for b in range(len_data, 0, -1):
                if a == b:
                    continue
                
                length = self.calcul_length(data[a], data[b])
                self.list_of_length.append(
                    (a, b, length)
                )
                if not self.vmax and not self.vmin:
                    self.vmax = (a, b, length)
                    self.vmin = (a, b, length)
                else:
                    self.vmax = (a, b, length)\
                        if length > self.vmax[2]\
                            else self.vmax
                

                    self.vmin = (a, b, length)\
                        if length < self.vmin[2] \
                            else self.vmin
            data.pop()
            len_data -= 1

        print(self.vmax)
        print(self.vmin)
        print(sys.getsizeof(self.list_of_length))
        print(datetime.now() - now)


class CalculateNumpy:
    vmin = None
    vmax = None
    list_of_length = np.array([])

    def calcul_length(self, a: list, b: list):
        square = np.square(a - b)
        return np.sum(square) 

    def __init__(self, data: list):
        print(sys.getsizeof(data))
        now = datetime.now()
        len_data = len(data) -1
        for a in range(len_data, 0, -1):
            for b in range(len_data, 0, -1):
                if a == b:
                    continue
                
                length = self.calcul_length(data[a], data[b])
                np.append(self.list_of_length, length)
                if not self.vmax and not self.vmin:
                    self.vmin = self.vmax = (a, b, length)
                else:
                    self.vmax = (a, b, length) if length > self.vmax[2] else self.vmax
                    self.vmin = (a, b, length) if length < self.vmin[2] else self.vmin
            len_data -= 1
            data = data = np.delete(data, len(data)-1, 0)
        print(self.vmax)
        print(self.vmin)
        print(sys.getsizeof(self.list_of_length))
        print(datetime.now() - now)
