from input_generator import InputGenerator
from calculate import Calculate, CalculateNumpy

# Создание файла CSV
# output = InputGenerator(name='vector.csv')
# output.create_vector(n=503, m=55)

# Чтение файла CSV

input_data = InputGenerator().open()

# Вычисление
print('Вычисление без Numpy')
Calculate(input_data)


# Чтение файла CSV
input_data_numpy = InputGenerator().open_as_numpy()

# Вычисление
print('Вычисление c Numpy')
CalculateNumpy(input_data_numpy)