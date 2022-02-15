import numpy as np


class CalculateNumpy:
    vmin = None
    vmax = None
    distribution = np.array([])

    def calcul_length(self, a, b):
        square = np.square(a - b)
        return np.sum(square)
    
    def set_min_max(self, a, b, distance):
        if not self.vmax and not self.vmin:
            self.vmin = self.vmax = (a, b, distance)
        else:
            self.vmax = (a, b, distance) if distance > self.vmax[2] else self.vmax
            self.vmin = (a, b, distance) if distance < self.vmin[2] else self.vmin

    def __init__(self, data: list):
        start = len(data) - 1
        for a in range(start, 0, -1):
            for b in range(start, 0, -1):
                if a == b:
                    continue
                distance = self.calcul_length(data[a], data[b])
                np.append(self.distribution, distance)
                self.set_min_max(a, b, distance)
            start -= 1
            data = np.delete(data, a, 0)
