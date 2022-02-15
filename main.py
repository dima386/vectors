from input_generator import InputGenerator
from calculate import Calculate

# Создание файла CSV
# output = InputGenerator(name='vector.csv')
# output.create_vector(n=503, m=55)

# Чтение файла CSV
input_data = InputGenerator().open()

# Вычисление
Calculate(input_data)