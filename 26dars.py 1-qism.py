#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 14:58:32 2025

@author: adolat
"""
# Dasturlash asoslari

# SO`Z TOPISH O`YINI

# Muallif: Adolat Imomiddinova: ISOMIDDIN QIZI:

# 26-Dars: SO`Z TOPISH O`YINI

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words) 
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
           display_letter += letter
        else:
           display_letter += "-"

def play():
    word = get_word()
    # So`zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harfalar
    user_letters = ''
    print(f"Men {len(word)} xonali son uyladim. Topa olasizmi?")
    # print(word)
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
           print(f"SHu vaqtgacha kiritgan xarflaringiz: {user_letters}")

        letter = input("Xarf kiriting: ").upper()
        if letter in user_letters:
           print("Bu xarfni avval kiritgansiz. Boshqa xarf kiriting.")
           continue
        elif letter in word:
             word_letters.remowe(letter)






































































































































































