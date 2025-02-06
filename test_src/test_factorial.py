import pytest
from src.factorial import Factorial, factorial_de_zero, factorial_negatiu

def test_num_1():
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(1)
    
    assert resultat == 1

def test_num_2():
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(2)
    
    assert resultat == 2

def test_num_0():
    calculadora = Factorial()
    
    with pytest.raises(factorial_de_zero):
        assert calculadora.calcula_factorial(0) == 0

def test_num_negatiu():
    calculadora = Factorial()
    with pytest.raises(factorial_negatiu):
        assert calculadora.calcula_factorial(-2) == 6


def test_num_3():
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(3)
    
    assert resultat == 6   

def test_num_4():
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(4)
    
    assert resultat == 24  

def test_num_5():
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(5)
    
    assert resultat == 120  

def test_num_7():
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(7)
    
    assert resultat == 5040