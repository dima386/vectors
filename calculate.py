import numpy as np


class Calculate:
    vmin = None
    vmax = None
    distribution = []

    def calcul_distance(self, a, b):
        ''' 
        Расчет Эвклидова расстояния используя инструменты numpy
        '''
        square = np.square(a - b)
        return np.sum(square)
    
    def set_min_max(self, a, b, distance):
        '''
        Запись минимума и максима расстояний в аттрибуты объекта
        '''
        data = (a, b, distance)
        if self.vmax and self.vmin:
            if distance > self.vmax[2]:
                self.vmax = data
            if distance < self.vmin[2]:
                self.vmin = data
        else:
            self.vmin = data
            self.vmax = data
    
    def increment_freq(self, distance):
        '''
        Увеличивает частоту расстояния в массивe по индексу
        Диапазон допустимых расстояний 0.0:100.0
        что соответствует индексам массива 0:1000
        Длина 38.5 соответствует индексу 385
        '''
        index = int(distance * 10)
        self.distribution[index] += 1
        
    def __init__(self, data):
        # генерация массива с нулями для записи частот
        self.distribution = np.zeros(1000)

        start = len(data) - 1

        for a in range(start, 0, -1):
            for b in range(start, 0, -1):
                if a == b:
                    continue
                distance = self.calcul_distance(data[a], data[b])
                self.increment_freq(distance)
                self.set_min_max(a, b, distance)
            start -= 1
            data = np.delete(data, a, 0)
