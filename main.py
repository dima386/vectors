from input_generator import InputGenerator
from calculate import Calculate
from graph import plot


N = 502 # количество векторов
M = 55 # количество измерений

# Создание файла CSV
output = InputGenerator(name='vector.csv')
output.create_vector(n=N, m=M)


# Чтение файла CSV
input_data_numpy = InputGenerator().open_as_numpy()

# Вычисление
print('Вычисление расстояний')
result = Calculate(input_data_numpy)
vmax = result.vmax
vmin = result.vmin


print(f'Максимальное расстояние: {vmax[2]} между векторами с индексами {vmax[1]} {vmax[0]}')
print(f'Минимальное расстояние: {vmin[2]} между векторами с индексами {vmin[1]} {vmin[0]}')
plot(result.distribution)


