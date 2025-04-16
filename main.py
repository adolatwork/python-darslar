#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 05:24:40 2025

@author:adolat
"""

# Dasturlash asoslari

# Muallif: Imomiddinova Adolat:ISOMIDDIN QIZI:

# UTILGAN MAVZULAR YANI PYTHODA BARCHA FUNKSIYALAR QATNASHGAN AMALIYOT

name = 'Adolat'
age = 20

print(name, age)
print('Hello, my name is:', name)


number: int = 10
decimal: float = 2.5
text: str = 'Hello, world!'
active: bool = False

names: list = ['Adolat','Ali','Abdulaziz']
coordinates: tuple = (1.5, 2.5)
unique: set = {1,4,2,9}
data: dict = {'name': 'Adolat','age': 20}


name: str = 'Adolat'
age: int = 'Eleven'

print(age)

from typing import Final

VERSION: Final[str] = '1.0.12'
PI: Final[float] = 3.1415

from datetime import datetime

def show_date() -> None:


    print('This is the current date end time:')
    print(datetime.now())

    print('This is the current time:')
    print(datetime.now())

show_date()
show_date()

# from datetime import datetime

def greet(name: str) -> None: # usages
    print(f'Hello, {name}')


greet('Adolat')
greet('Abdulaziz')

def add(a: float, b: float) -> None: #1 usage
    print('Hello')

print(add(1, 2))


class Car: # 2 usages
    def __init__(self, colour: str, horsepower: int) -> None:
       self.colour = colour
       self.horsepower = horsepower

volvo: Car = Car('red', 200)
print(volvo.colour)
print(volvo.horsepower)

bmw: Car = Car('blue',240)
print(bmw.colour)
print(bmw.horsepower)

class Car: # usages
     def __init__(self,brand: str, horsepower: int) -> None:
         self.brand = brand
         self.horsepower = horsepower

     def drive(self) -> None:
         print(f'{self.brand} is driving!')

     def __str__(self) -> str:
         return f'{self.brand}, {self.horsepower}hp'
         
     def __add__(self, other: Self) -> str:
         return f'{self.brand} & {other.brand}'

     def __mul__(self,other):

     def get_info(self, var: int) -> None: # 1 usage
         print(var)
         print(f'{self.brand} with {self.horespower} horsepower ')

volvo: Car = Car('Volvo', 200)
bmw: Car =Car('BMW', 240)
print(volvo + bmw)
print(volvo * bmw)
volvo: Car = Car('Volvo', 200)
volvo.drive()
volvo.get_info(10)

# bmw: Car = Car('BMW', 240)
# bmw.drive()












































































































