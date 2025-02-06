'''pytest'''
import pytest
from src.factorial import Factorial, FactorialDeZero, FactorialNegatiu

def test_num_1():
    '''Test1'''
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(1)

    assert resultat == 1

def test_num_2():
    '''Test2'''
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(2)

    assert resultat == 2

def test_num_0():
    '''Test3'''
    calculadora = Factorial()  
    with pytest.raises(FactorialDeZero):
        assert calculadora.calcula_factorial(0) == 0

def test_num_negatiu():
    '''Test4'''
    calculadora = Factorial()
    with pytest.raises(FactorialNegatiu):
        assert calculadora.calcula_factorial(-2) == 6


def test_num_3():
    '''Test5'''
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(3)

    assert resultat == 6


def test_num_4():
    '''Test6'''
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(4)
    assert resultat == 24


def test_num_5():
    '''Test7'''
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(5)

    assert resultat == 120


def test_num_7():
    '''Test8'''
    calculadora = Factorial()
    resultat = calculadora.calcula_factorial(7)

    assert resultat == 5040
