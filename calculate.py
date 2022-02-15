from array import array
import numpy as np
from datetime import datetime


class CalculateNumpy:
    vmin = None
    vmax = None
    distribution = []

    def calcul_length(self, a, b):
        square = np.square(a - b)
        return np.sum(square)
    
    def set_min_max(self, a, b, distance):
        data = (a, b, distance)
        if self.vmax and self.vmin:
            if distance > self.vmax[2]:
                self.vmax = data
            if distance < self.vmin[2]:
                self.vmin = data
        else:
            self.vmin = data
            self.vmax = data

    def __init__(self, data: list):
        start = len(data) - 1
        for a in range(start, 0, -1):
            for b in range(start, 0, -1):
                if a == b:
                    continue
                distance = self.calcul_length(data[a], data[b])
                self.distribution.append(distance)
                self.set_min_max(a, b, distance)
            start -= 1
            data = np.delete(data, a, 0)
