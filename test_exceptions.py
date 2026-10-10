import pytest
from Exceptions import ExceptionsDemo, MyException  

@pytest.mark.unit
def test_divide_zero():
    demo= ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)

@pytest.mark.unit
def test_Type_error():
    demo= ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide('Tamaulipas', 5)
        
@pytest.mark.unit
def test_index_error():
    demo= ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([3,4,5], 7)

@pytest.mark.unit
def test_index_error():
    demo= ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([3,4,5], 7)

@pytest.mark.unit
def test_index_type_error():
    demo= ExceptionsDemo()
    with pytest.raises(TypeError, IndexError):
        demo.access_list([3,4,5], 7)
        demo.access_list([3,4,5], 1)

@pytest.mark.unit
def test_key_error():
    demo= ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({'manzana': 'dulce'}, 'tomate')

@pytest.mark.unit
def test_FileNotFound_error():
    demo= ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file('rex.txt')

@pytest.mark.unit
def test_access_atribute_error():
    demo= ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(object())

@pytest.mark.unit
def test_my_exception_error():
    demo= ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-2)

@pytest.mark.wip
def test_my_exception_error():
    demo= ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-2)
