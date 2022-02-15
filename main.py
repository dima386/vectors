from input_generator import InputGenerator
from calculate import CalculateNumpy

# Создание файла CSV
# output = InputGenerator(name='vector.csv')
# output.create_vector(n=503, m=55)


# Чтение файла CSV
input_data_numpy = InputGenerator().open_as_numpy()

# Вычисление
print('Вычисление c Numpy')
result = CalculateNumpy(input_data_numpy)
print(result.vmax)
print(result.vmin)