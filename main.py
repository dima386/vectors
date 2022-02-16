from input_generator import InputGenerator
from calculate import Calculate
from graph import Graph


N = 502 # количество векторов
M = 55 # количество измерений
FILENAME = 'vector.csv'


# Создание файла CSV
output = InputGenerator(name=FILENAME)
output.create(n=N, m=M)


# Чтение файла CSV
input = InputGenerator(name=FILENAME).open()


# Вычисление
print('Вычисление расстояний')
res = Calculate(input)


print(f'Максимальное расстояние: {res.vmax[2]} между векторами с индексами {res.vmax[1]} {res.vmax[0]}')
print(f'Минимальное расстояние: {res.vmin[2]} между векторами с индексами {res.vmin[1]} {res.vmin[0]}')


# Построение графика рапределения
Graph.plot(res.distribution)


