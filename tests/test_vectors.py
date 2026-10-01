from mathlab.Vectors import Vector
import pytest

def test_create():
    v1 = Vector([1,3,4])

    assert v1.values == [1,3,4]
def test_empty():
    with pytest.raises(ValueError):
        Vector([])
def test_type():
    with pytest.raises(TypeError):
        Vector(['123',23,4])
def test_add():
    v1 = Vector([7,2,3]) 
    v2 = Vector([4,43,2])
    res = v1 + v2
    assert res.values == [11,45,5]
def test_add_notVector():
    v1 = Vector([7,2,3]) 
    with pytest.raises(TypeError):
         v1 + 5
def test_diff_razmer():
    v1 = Vector([7,2,3]) 
    v2 = Vector([4,43,2,6])
    with pytest.raises(ValueError):
        v1 + v2
def test_diff_razmer2():
    v1 = Vector([7,2,3,6]) 
    v2 = Vector([4,43,2])
    with pytest.raises(ValueError):
            v1 + v2  
def test_sub():
    v1 = Vector([7,2,3]) 
    v2 = Vector([4,43,2])
    res = v1 - v2
    assert res.values == [3,-41,1]
def test_sub_notVector():
    v1 = Vector([7,2,3]) 
    with pytest.raises(TypeError):
         v1 - 5
def test_subdiff_razmer():
    v1 = Vector([7,2,3]) 
    v2 = Vector([4,43,2,6])
    with pytest.raises(ValueError):
        v1 - v2
def test_subdiff_razmer2():
    v1 = Vector([7,2,3,6]) 
    v2 = Vector([4,43,2])
    with pytest.raises(ValueError):
            v1 - v2  
def mul():
    v1 = Vector([7,2,3]) 
    res = v1 * 3
    assert res.values == [21,6,9]
def test_mul_type():
    v1 = Vector([7,2,3]) 
    with pytest.raises(TypeError):
        v1 * '12'
def test_mul_type2():
    v1 = Vector([7,2,3,6]) 
    with pytest.raises(TypeError):
            v1 * False 
def div():
    v1 = Vector([12,6,3]) 
    res = v1 / 3
    assert res.values == [4,2,1]
def test_div_type():
    v1 = Vector([7,2,3]) 
    with pytest.raises(TypeError):
        v1 / '12'
def test_div_type2():
    v1 = Vector([7,2,3,6]) 
    with pytest.raises(TypeError):
            v1 / False 
def test_div_value():
    v1 = Vector([7,2,3,6]) 
    with pytest.raises(ZeroDivisionError):
            v1 / 0
def test_eq_diffrazmer():
    v1 = Vector([7,2,3]) 
    v2 = Vector([7,2,3,6])
    assert v1 != v2 
def test_eq_notVector():
    v1 = Vector([7,2,3]) 
    assert v1 != 8
def test_eq_notVector2():
    v1 = Vector([7,2,3]) 
    assert v1 != "8"
def test_dot():
    v1 = Vector([7,2,3,6])
    v2 = Vector([6,4,3,2])
    assert v1.dot(v2) == 71
def test_dot_Type():
    v1 = Vector([7,2,3,6]) 
    with pytest.raises(TypeError):
            v1.dot(5) 
def test_dot_Type2():
    v1 = Vector([7,2,3,6]) 
    with pytest.raises(TypeError):
            v1.dot('5')
def test_dot_razmer():
    v1 = Vector([7,2,3,6])
    v2 = Vector([6,3,2])
    with pytest.raises(ValueError):
                v1.dot(v2)                      
def test_dist_razmer():
    v1 = Vector([7,2,3,6])
    v2 = Vector([6,3,2])
    with pytest.raises(ValueError):
                v1.dist_to(v2)
def test_dist_type():
    v1 = Vector([7,2,3,6])
    with pytest.raises(TypeError):
                v1.dist_to('v2')
def test_dist():
    v1 = Vector([7,2,3])
    v2 = Vector([6,3,2])
    assert v1.dist_to(v2) == 1.7320508075688772
def test_normaliz():
    v1 = Vector([7,2,3])
    assert v1.normalized().values == [0.8890008890013334, 0.254000254000381, 0.3810003810005715]
def test_normaliz_nullVector():
    v1 = Vector([0,0,0])
    with pytest.raises(ValueError):
         v1.normalized()