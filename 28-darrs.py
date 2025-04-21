#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 09:52:16 2025

@author: adolat
"""
# Dasturlash asoslari:

# Muallif:Imomiddinova Adolat: ISOMIDDIN QIZI

# 28_DARS KLASSLAR

# x=10
# print(type(x))
# matn = "salom"
# print(type(matn))
# print(matn.upper())

# def salom():
#     print("Assalomu alaykum")

# print(type(salom))

class Talaba:
     def __init__(self,ism,familiya,tyil):
         self.ism = ism
         self.familiya = familiya
         self.tyil = tyil
    
     def get_name(self):  
         return self.ism
         
     def get_age(self,yil):
         return yil - self.tyil
    
     def tanishtir(self):
         return(f"Ismim {self.ism}.{self.familiya}.{self.tyil} yilda tug`ilganman")

talaba1 = Talaba("Olim","Olimov",2000)
talaba2 = Talaba("Husan","Husanov",1995)
talaba3 = Talaba("Akrom","Alimov",2004)











































































































































































