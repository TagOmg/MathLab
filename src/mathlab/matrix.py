class Matrix:
    def __init__(self,values):
        if len(values) == 0:
            raise ValueError('Пустая матрица')
        elif not all([isinstance(num, (int, float)) and not isinstance(num, bool) for x in values for num in x]):
            raise TypeError('Неверный тип данных') 
        for x,y in enumerate(values):
            if x + 1 < len(values) and len(values[x]) != len(values[x+1]):
                raise ValueError('Разная длина строк') 
        self.values = values
    def __str__(self):
        return f'{*self.values}/n'
A = Matrix([[1,4,5,6],[5,7,3,5],[1,5,6,7],[1,4,5,5]])
print(A)