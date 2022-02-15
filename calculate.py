import sys


class Calculate:
    min_val = None
    max_val = None
    list_of_length = []

    def calcul_length(self, a: list, b: list):
        length = sum(((float(a[i]) - float(b[i])) ** 2 for i, _ in enumerate(a)))
        return length 

    def __init__(self, input_data: list):
        print(sys.getsizeof(input_data))
        len_data = len(input_data) -1
        for i_a in range(len_data, 0, -1):
            for i_b in range(len_data, 0, -1):
                if i_a == i_b:
                    continue
                
                length = self.calcul_length(input_data[i_a], input_data[i_b])
                self.list_of_length.append(
                    (i_a, i_b, length)
                )
                if not self.max_val and not self.min_val:
                    self.max_val = (i_a, i_b, length)
                    self.min_val = (i_a, i_b, length)
                else:
                    self.max_val = (i_a, i_b, length)\
                        if length > self.max_val[2]\
                            else self.max_val
                

                    self.min_val = (i_a, i_b, length)\
                        if length < self.min_val[2] \
                            else self.min_val
            input_data.pop()
            len_data -= 1

        print(self.max_val)
        print(self.min_val)
        print(sys.getsizeof(self.list_of_length))
        print(len(self.list_of_length))