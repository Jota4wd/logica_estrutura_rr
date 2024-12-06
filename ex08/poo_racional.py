import math
import os

os.system('clear')

class Racional:
    def __init__(self, divisor, dividendo):
        self.divisor = divisor
        self.dividendo = dividendo


    def __str__(self):
        return str(f'{self.divisor} / {self.dividendo}' )


    def __mul__(self, outro):
        divisor = self.divisor * outro.divisor
        dividendo = self.dividendo * outro.dividendo
        return Racional(divisor, dividendo)


a = Racional(1, 2)
b = Racional(3, 4)

c = a*b

print(a)
print(b)
print(c)
print(a*b)
