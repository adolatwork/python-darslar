#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 14:28:30 2025

@author: adolat
"""

# Dasturlash asoslari

# 35-DARS: XATOLAR BILAN ISHLASH

# Muallif: Imomiddinova Adolat: ISOMIDDIN QIZI

yosh = input("Yoshingizni kiriting: ")

try:
    yosh = int(yosh)
except ValueError:
      print("Siz butun son kiritmadingiz ")
else:
     print("Siz {2025-yosh} yilda tug`ilgansiz")

print("Dastur davom etayapti")   
print("Dastur tugadi")


mevalar = ['olma','anor','uzum','anjir',]
try:
    print(mevalar[4])
except IndexError:
     print(f"Ro`yxatdan {len(mevalar)} ta meva bor xolos")

user = {"username":"sariqdev",
        "status":"admin",
        "email":"admin@sariq.dev",
        "phone":"99897123456"}

key="email"
try:
     print(f'foydalanuvchi: {user[key]}')
except KeyError:
     print("Bunday kalit mavjud emas") 

print(user['username'])


filename = "data.txt" # bunday fayl mavjud emas
try:
    with open(filename) as f:
         txt = f.read()
except FileNotFoundError:
      print(f"{filename} mavjud emas")


import json
files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
for filename in files:
    try:
       with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
          pass
    else:
         print(talaba['ism'])
         # fayl ustida turli amallar


n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError: # agar foydalanuvchi butun son 
     print("Butun son kiritmadingiz")
except ZeroDivisionError:
     print("0 ga bo`lish mumkin emas")
else:
    print(f"x={x}")

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
       yosh = int(yosh)
       break

print(f"Siz {2025-yosh} yilda tug`ilgansiz")


#  AMALIYOT




























































