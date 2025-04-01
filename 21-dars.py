#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 09:56:50 2025

@author: adolat
"""
# Dasturlash asoslari
# 21-dars:  FUNKSIYAGA RUYXAT UZATISH
# Muallif: Adolat


# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#          ism = ismlar.pop()
#          baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
#          baholar[ism]=int(baho)
#     return baholar

# talabalar = ['ali', 'abdulaziz','adolat','mustafo']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)


# Amaliyot
import random

def qiziqarli_javob(ismlar):
    # Tasodifiy ismni tanlash
    tanlangan_ism = random.choice(ismlar)
    javoblar = [
         f"{tanlangan_ism.title()} - Bu ism menga juda yoqadi!",
         f"{tanlangan_ism.title()} - Bu ism juda noodatiy tuyuladi!",
         f"{tanlangan_ism.title()} - Bu ismni eshitganimda yuragim g`alati bo`lib ketadi!",
         f"{tanlangan_ism.title()} - Bu  ism juda ko`p ma`nolarni anglatadi!",
         f"{tanlangan_ism.title()} - Bu ismni tanlaganingizga qoyil qoldim!"
    ]

    # Tasodiy javobni tanlash
    javob = random.choice(javoblar)
    return javob

def asosiy():
    ismlar = []
    print("Ismlar ro`yxatini kiriting (to`xtash uchun 'stop' deb yozing):")
    while True:
        ism = input("Ism kiriting: ").strip()
        if ism.lower() == 'stop':
           break
        if ism:
             ismlar.append(ism)

    if ismlar:
        javob = qiziqarli_javob(ismlar)
        print("\nNatija:")
        print(javob)
    else:
        print("Siz birorta ham ism kiritmadingiz.")

# Dastur ishga tushishi uchun:
asosiy()



# ❌





























































































































