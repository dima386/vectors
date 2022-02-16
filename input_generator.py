import os
import numpy as np


class InputGenerator:
    '''
    Класс для быстрого чтения файлов векторов
    '''
    name = 'vector.csv'
    folder = 'input'
    
    def __init__(self, name=name, **kwargs):
        self.name = name
        self.full_path = self.get_path()
    
    def get_path(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        return os.path.join(self.folder, self.name)
    
    def create(self, n, m):
        assert (n and 500 < n <= 1000), 'n must be in range 501:1000'
        assert (m and 10 < m <= 100), 'm must be in range 11:100'
        data = np.random.uniform(-1.0, 1.0, (n, m))
        np.savetxt(self.full_path, data, delimiter=",")

    def open(self):
        return np.genfromtxt(self.full_path, delimiter=',')
