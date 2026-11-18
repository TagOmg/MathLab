class Matrix:
    def __init__(self,values):
        if len(values) == 0 or any(len(row) == 0 for row in values):
            raise ValueError('Пустая матрица')
        
        elif not all([isinstance(num, (int, float)) and not isinstance(num, bool) for x in values for num in x]):
            raise TypeError('Неверный тип данных') 
        
        for x,y in enumerate(values):
            if x + 1 < len(values) and len(values[x]) != len(values[x+1]):
                raise ValueError('Разная длина строк') 
            
        self.values = values

    def __str__(self):
        matrix = ''
        ln = [0] * len(self.values[0])

        for row in self.values:
            row = map(str,row)

            for index,columns in enumerate(row):
                if len(columns) > ln[index]:
                    ln[index] = len(columns)

        for row in self.values:
            row = map(str,row)
            format_row = []

            for index,element in enumerate(row):
                format_row.append(element.rjust(ln[index]))

            matrix += ' '.join(format_row) + '\n'
        return matrix[:-1]

    
    def __add__(self,other):
        new  = []

        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            raise ValueError('Матрицы разных размерностей')
       
        for index,row in enumerate(self.values):
                new.append([x+y for x,y in zip(row,other.values[index])])

        return Matrix(new)

    
    def __mul__(self,scalar):
        new = []
        
        if not isinstance(scalar, (int, float)) or isinstance(scalar, bool) :
            raise TypeError('Неверный тип')

        for row in self.values:
            new_elements = []
            for element in row:
                new_elements.append(element * scalar)
            new.append(new_elements)

        return Matrix(new)

    
    def __truediv__(self,scalar):
            if not isinstance(scalar, (int, float)) or isinstance(scalar, bool) :
                raise TypeError('Неверный тип')
            elif scalar == 0:
                raise ZeroDivisionError('Деление на ноль')
            return self * (1/scalar)

    
    def __sub__(self, other):
            return self + other * -1

    
    def transpose(self):
        trans = []
        for row in zip(*self.values):
            trans.append(list(row))
        return Matrix(trans)


    def __matmul__(self, other):
        from mathlab.vector import Vector
        is_vector = False

        if len(self.values[0]) != len(other.values):
            raise ValueError('Не подходящие размеры матриц')
        elif type(other) is Vector:
            other = Matrix([[coord] for coord in other.values])
            is_vector = True

        new_matrix = []
        other_values_trans = other.transpose().values

        for row1 in self.values:
            new_row = []

            for row2 in other_values_trans:
                new_row.append(sum(x * y for x, y in zip(row1,row2)))
            new_matrix.append(new_row)

        if is_vector:
            return Vector([row[0] for row in new_matrix])
        else:
            return Matrix(new_matrix)
