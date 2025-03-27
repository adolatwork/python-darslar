#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 07:20:10 2025

@author: adolat
"""
# Dasturlash asoslari
# Muallif:Imomiddinova Adolat:Isomiddin qizi:
# 25-dars:"SON TOPISH O`YINI"
# BISMILLAX 7

import random
import time

def player_gusses():
    print("🎮 O`YIN BOSHLANDI! Keling birinchi bosqichni boshlaymiz!")
    print("🤖 men 10 dan 15 gacha bir son uyladim.Topishga urinib ko`ring!🚀")

    secret_number = random.randint(10,15)
    attempts = 0

    while True:
         guess = int(input("\n🎯 Taxminingizni kiriting: "))
         attempts += 1

         if guess < secret_number:
             print("🔺Yo`q bu son juda kichik! Kattroq son kiritng! 💪")
         elif guess > secret_number:
             print("🔻 Afsus bu sson juda katta! Kichikroq son kiriting! 😎")
         else:
             print(f"\n🎉 Tabriklayman! 🎯 {guess} sonini {attempts} ta urinishda topdingiz! 👏👏👏")
             break

          # chegaralarni tekshirish
         if low > high:
             print("CHegaralar noto`g`ri belgilandi. Dastur tugatildi.")
             break 

def computer_guess():
    print("2. Endi siz bir son o`ylaysiz, men esa uni topishga harakat qilaman! 😎")
    
    secret_number = int(input("10 dan 15 gacha bo`gan bir son o`ylang (men topaman):"))

    low, high = 10, 15
    attempts = 0,
   
    while True:
        guess = random.randint(low,high)
        print(f"🤖 Men {guess} sonini taxmin qildim.")
        attempts += 1

        if guess < secret_number:
           print("🔼 Men o`ylagan soningiz kattaroq ekan! ")
           low = guess + 1
        elif guess > secret_number:
            print("🔽 Men o`ylagan soningiz kichikroq ekan! ")
            high = guess - 1
        else:
            print(f"🎯 Yashasin! Men {guess} sonini {attempts} ta urinishda topdim 🚀\n")
            break

def player_guess():
    print("O`yinchi sonni topishga harakat qilmoqda...")


def main():
    print("🔢 SON TOPISH O`YINIGA XUSH KELIBSIZ! 🔢")
    print("Bu o`yinda men siz o`ylagan sonni topaman va siz men o`ylagan sonni topishga harakat qilasiz. 😄\n")

    player_guess()   

 # main funksiyasini chaqirish
if __name__=="__main__":
    main()











































































































































