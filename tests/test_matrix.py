from mathlab.matrix import Matrix
from mathlab.vector import Vector

import pytest

def test_create():
    A = Matrix([[1,3,4]])

    assert A.values == [[1,3,4]]


def test_create2():
    A = Matrix([[1,3,4],[1,3,4]])
    assert A.values == [[1,3,4],[1,3,4]]


def test_create3():
    with pytest.raises(TypeError):
            Matrix([[24,5,6], 4])



def test_empty():
    with pytest.raises(ValueError):
        Matrix([[]])


def test_empty1():
    with pytest.raises(ValueError):
        Matrix([[],[]])



def test_empty2():
    with pytest.raises(ValueError):
        Matrix([])


def test_empty3():
    with pytest.raises(ValueError):
        Matrix([[1,45,5], []])

def test_type():
    with pytest.raises(TypeError):
        Matrix([['123',23,4]])


def test_type2():
    with pytest.raises(TypeError):
        Matrix([[True,23,4]])


def test_lenght():
    with pytest.raises(ValueError):
            Matrix([[1,3,4],[1,3,4,5]])

def test_add():
    A = Matrix([[2,4,7],[4,3,2]])
    B = Matrix([[6,1,2],[3,9,4]])
    assert (A+B).values == [[8,5,9],[7,12,6]]


def test_add2():
    A = Matrix([[2,-4,7],[4,3,-2]])
    B = Matrix([[-6,1,2],[3,-9,4]])
    assert (A+B).values == [[-4,-3,9],[7,-6,2]]


def test_add3():
    A = Matrix([[2,-4,7],[4,3,-2]])
    B = Matrix([[-6,1,2,7],[3,-9,4,6]])
    with pytest.raises(ValueError):
            A+B


def test_mul():
    A = Matrix([[2,4,7],[4,3,2]])
    assert (A * 3).values == [[6,12,21],[12,9,6]]


def test_mul2():
    A = Matrix([[2,4,7],[4,3,2]])
    assert (A * (1/2)).values == [[1.0,2.0,3.5],[2.0,1.5,1.0]]


def test_mul3():
    A = Matrix([[2,4,7],[4,3,2]])
    with pytest.raises(TypeError):
        A * True


def test_mul4():
    A = Matrix([[2,4,7],[4,3,2]])
    with pytest.raises(TypeError):
        A * '23'


def test_mul5():
    A = Matrix([[2,4,7],[4,3,2]])
    assert (A * 0.5).values == [[1.0,2.0,3.5],[2.0,1.5,1.0]]


def test_mul6():
    A = Matrix([[2,4,7],[4,3,2]])
    assert (A * 0).values == [[0,0,0],[0,0,0]]


def test_mul7():
    A = Matrix([[2,4,7],[4,3,2]])
    assert (A * -3).values == [[-6,-12,-21],[-12,-9,-6]]


def test_div():
        A = Matrix([[2,4,7],[4,3,2]])
        assert (A / 2).values == [[1.0,2.0,3.5],[2.0,1.5,1.0]]


def test_div2():
        A = Matrix([[2,4,7],[4,3,2]])
        assert (A / -2).values == [[-1.0,-2.0,-3.5],[-2.0,-1.5,-1.0]]


def test_div3():
    A = Matrix([[2,4,7],[4,3,2]])
    with pytest.raises(TypeError):
        A / True


def test_div4():
    A = Matrix([[2,4,7],[4,3,2]])
    with pytest.raises(TypeError):
        A / '23'


def test_div5():
    A = Matrix([[2,4,7],[4,3,2]])
    with pytest.raises(ZeroDivisionError):
        A / 0
def test_sub():
    A = Matrix([[2,4,7],[4,3,2]])
    B = Matrix([[6,1,2],[3,9,4]])
    assert (A-B).values ==[[-4,3,5],[1,-6,-2]]
def test_sub2():
    A = Matrix([[2,4,7],[4,3,2]])
    B = Matrix([[-6,-1,-2],[-3,-9,-4]])
    assert (A-B).values == [[8,5,9],[7,12,6]]
def test_transpose():
    B = Matrix([[6,1,2],[3,9,4]])
    assert B.transpose().values == [[6,3],[1,9],[2,4]]
def test_matmul():
    A = Matrix([[2,4,7],[4,3,2]])
    B = Matrix([[6,1,2],[3,9,4],[3,5,6]])
    assert (A@B).values == [[45, 73, 62], [39, 41, 32]]
def test_matmul2():
    A = Matrix([[2,4],[4,3]])
    B = Matrix([[6,1],[3,9]])
    assert (A@B).values == [[24, 38], [33, 31]]
def test_matmul3():
    A = Matrix([[2,4,6],[4,3,5]])
    B = Matrix([[6,1],[3,9]])
    with pytest.raises(ValueError):
        A@B
def test_matmul2():
    A = Matrix([[2,4],[-4,3]])
    B = Matrix([[-6,1],[3,-9]])
    assert (A@B).values == [[0, -34], [33, -31]]
def test_matrix_matmul_vector():
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])
    vector = Vector([2, 3, 4])

    result = matrix @ vector

    assert result.values == [20, 47]
    assert isinstance(result, Vector)

def test_matrix_matmul_vector_with_negative_numbers():
    matrix = Matrix([
        [1, -2],
        [0, 3]
    ])
    vector = Vector([-2, 4])

    result = matrix @ vector

    assert result.values == [-10, 12]

def test_matrix_matmul_vector_with_zeros():
    matrix = Matrix([
        [0, 0],
        [1, 2]
    ])
    vector = Vector([5, 3])

    result = matrix @ vector

    assert result.values == [0, 11]

def test_matrix_matmul_vector_incompatible_dimensions():
    matrix = Matrix([
        [1, 2],
        [3, 4]
    ])
    vector = Vector([1, 2, 3])

    with pytest.raises(ValueError):
        matrix @ vector

def test_matrix_matmul_vector_does_not_modify_original():
    matrix = Matrix([
        [1, 2],
        [3, 4]
    ])
    vector = Vector([5, 6])

    original_matrix = [row[:] for row in matrix.values]
    original_vector = vector.values[:]

    matrix @ vector

    assert matrix.values == original_matrix
    assert vector.values == original_vector
