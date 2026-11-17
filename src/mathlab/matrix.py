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
