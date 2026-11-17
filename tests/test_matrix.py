from mathlab.matrix import Matrix
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
