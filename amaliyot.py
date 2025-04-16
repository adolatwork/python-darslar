#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:32:41 2025

@author: adolat
"""

# Dasturlash asoslari

# Muallif:  Adolat Imomiddinova: ISOMIDDIN QIZI:

# ODDIY AMALIYOT

name = 'Adolat'

age = 20


print(name,age)
print('Hello, my name is:', name)

number: int = 10
decimal: float = 2,5
text: str = 'Hello, world!'
active: bool = False

names: list = ['Adolat','Ali','Abdulaziz']
coordinates: tuple = (1.5, 2.5)
uniqu: set = {1, 4, 2, 9}
data: dict ={'name': 'Adolat', 'age':20}

name: str = 'Adolat'
age: int = 'Eleven'

print(age)

from typing import Final

VERSION: Final[str] = '1.0.12'
PI: Final[float] = 3.1415

from datetime import datetime

def show_date() -> None: 
    print('This is the current date ')
    print(datetime.now())
   
show_date() 
show_date()

# from datetime import datetime


def greet(name:str) -> None: # 2 usages
    print(f'Ciao, {name}!')

greet('Adolat')
greet('Abdulaziz')

def add(a: float, b: float) -> float: # usage
    return a + b

print(add( 1, 2))






























































