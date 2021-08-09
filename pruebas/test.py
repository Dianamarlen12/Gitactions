import pytest
import test as t

#ARRAY ELABORADO
array = [5,3,4,2,1]
#DICCIONARIO CON LOS DATOS QUE SE AGREGARON
diccionario = [
    {"nombre":"Marlen","edad":21},
    {"nombre":"Dania","edad":18},
    {"nombre":"Josue","edad":22}]

def test_arreglo():
    assert t.order(array) == [1,2,3,4,5]

def test_mayores():
    assert t.count_mayores(diccionario) == 2