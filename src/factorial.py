'''Desenvolupa la funció factorial mitjançant la metodologia TDD.'''

class FactorialDeZero(Exception):
    '''Error factorial de zero'''

class FactorialNegatiu(Exception):
    '''Error factorial negatiu'''

# pylint: disable=R0903
class Factorial():
    '''Clase Factorial'''

    def __init__(self):
        pass


    def calcula_factorial(self, num):
        '''Mètode per calcular el factorial'''
        if num == 0:
            raise FactorialDeZero(
                'No hi ha factorial de zero: sempre seria zero')
        if num<0:
            raise FactorialNegatiu('No hi ha factorials negatius')
        if num<=2:
            return num
        else:
            return num * self.calcula_factorial(num-1)
