#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 08:44:18 2025

@author: adolat
"""

# Dasturlash asoslari
# Muallif: Imomiddinova Adolat:ISOMIDDIN QIZI:
# 25-dars: 3-qism
# SON TOPISH O`YINI

import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o`yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
           print("Xato. Men o`ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
             print("Xato. Men o`ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
           break
    return taxminlar
    print(f"Tabriklaymiz.{taxminlar} ta taxmin Topdingiz!")

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o`ylang va istalgan tugmani bosing. Men topaman")
    quyi = 1
    yuqori = x
    taxminlar = 0 
    while True:
        taxminlar += 1
        if quyi != yuqori:
           taxmin = random.randint(quyi, yuqori)
        else:
           taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o`yladingiz: to`g`ri (t),"
                      f"men o`ylagan son bundan kattaroq (+), yoki kichikroq (-)". lower())
        if javob == "-":
           yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while True:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop(x)

        if taxminlar_user>taxminlar_pc:
           print("Men yutdim!")
        elif taxminlar_user<taxminlar_pc:
           print("Siz yutdingiz!")
        else:
           print("Durrang!")
        yana = int(input("Yana o`ynaysizmi? Ha(1)/Yo`q(0):"))

play()

























































































































































