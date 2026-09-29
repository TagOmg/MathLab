import pytest
class Vector:
    def __init__(self,values):
        self.values = list(values)

    def __str__(self):
        res = ', '.join(map(str,self.values))
        return f'Vector coordinates: {res}'
    
    def __getitem__(self,index):
        return self.values[index]
    
    def __len__(self):
        return len(self.values)
    
    def __add__(self, plus):
        if len(self.values) != len(plus.values):
            raise ValueError('Векторы разной размерности')
        
        return Vector([x + y for x, y in zip(self.values, plus.values)])
    
    def __sub__(self, minus):
            if len(self.values) != len(minus.values):
                raise ValueError('Векторы разной размерности')
            
            return Vector([x - y for x, y in zip(self.values, minus.values)])
    
    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.values])

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError('Деление на ноль')
        return Vector([x / scalar for x in self.values])
    def __neg__(self):
        return Vector([-x for x in self.values])
    def __eq__(self, other):
        TF =[x ==y for x,y in zip(self.values,other.values )]
        return True if sum(TF) == len(TF) else False
    def dot(self,other):
        return sum([x  * y for x,y in zip(self.values,other.values )])
    def norm(self):
        return sum([x**2 for x in self.values])**0.5
    def dist(self,other):
       a = [x - y for x,y in zip(self.values,other.values )]
       return sum(map(pow,a, [2]*len(a)))**0.5
    def normalized(self):
        return Vector([x / self.norm() for x in self.values])
v1 = Vector([1,2])
v2 = Vector([4,6])
v3 = Vector([4, 3, 2])
print(v1.normalized().norm())