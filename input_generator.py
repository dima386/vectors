import csv
import os
import random
import numpy as np


class InputGenerator:
    '''
    Класс для быстрого чтения файлов векторов
    '''
    name = 'vector.csv'
    folder = 'input'
    random_range = (-1, 1)
    delimiter = ','
    
    def __init__(self, name=name, **kwargs):
        self.name = name
        self.full_path = self.get_path()
    
    def get_path(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        return os.path.join(self.folder, self.name)
    
    def create_vector(self, n, m):
        assert (n and 500 < n <= 1000), 'n must be in range 501:1000'
        assert (m and 10 < m <= 100), 'm must be in range 11:100'
        with open(self.full_path, 'w', newline='') as csvfile:
            output = csv.writer(csvfile, delimiter=self.delimiter, quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for _ in range(n):
                vector = (random.uniform(*self.random_range) for _ in range(m))
                output.writerow(vector)
    
    def open(self):
        with open(self.full_path, newline='') as csvfile:
            return list(csv.reader(csvfile, delimiter=',', quotechar='|'))
    
    def open_as_numpy(self):
        return np.genfromtxt(self.full_path, delimiter=',')
