from input_generator import InputGenerator
from calculate import CalculateNumpy
from plot import plot_graph
import numpy as np

N = 502 # количество векторов
M = 20 # количество измерений

# Создание файла CSV
output = InputGenerator(name='vector.csv')
output.create_vector(n=N, m=M)


# Чтение файла CSV
input_data_numpy = InputGenerator().open_as_numpy()

# Вычисление
print('Вычисление расстояний')
result = CalculateNumpy(input_data_numpy)
vmax = result.vmax
vmin = result.vmin
distribution = np.array(result.distribution)



print(f'Максимальное расстояние: {vmax[2]} между векторами с индексами {vmax[1]} {vmax[0]}')
print(f'Минимальное расстояние{vmin[2]} между векторами с индексами {vmin[1]} {vmin[0]}')
plot_graph(distribution, vmin, vmax)


