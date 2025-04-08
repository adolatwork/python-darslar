#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 14:54:47 2025

@author: adolat
"""
# Dasturlash asoslari
# Muallif:Adolat Imomiddinova:ISOMIDDIN QIZI:
# SON TOPISH O`YINI

import random
print("🔢 SON TOPISH O`YINI BOSHLANDI 🔢")
print("1️⃣ Men son o`ylayman, siz topasiz")
print("2️⃣ Siz son o`ylaysiz, men topaman")

tanlov = input("\nQaysi o`yinni o`ynaymiz? (1,yoki 2):")

if tanlov == "1":
    print("\Men 1 dan 100 gacha son o`yladim. Uni topishga harakat qiling!")
    kompyuter_soni = random.randint(1, 100)
    urinishlar = 0

    while True:
        urinishlar += 1
        foydalanuvchi_soni = int(input(f"{urinishlar}-urinish: Son kiriting:"))

        if foydalanuvchi_soni < kompyuter_soni:
            print("📈 Kattaroq son o`ylang!")
        elif foydalanuvchi_soni > kompyuter_soni:
            print("📉 Kichikroq son o`ylang!")
        else:
            print(f"🎉 Tabriklayman! Siz {urinishlar} ta urinishda topdingiz!🎊")
            print("😎 Siz juda yaxshi o`ynadingiz!")
            break

elif tanlov == "2":
     print("\nSiz 1 dan 100 gacha bir son o`ylang. Men topishga harakat qilaman.")
     past = 1
     yuqori = 100
     urinishlar = 0

     input("Sonni o`ylagan bo`lsangiz, ENTER bosing...")

     while True:
          urinishlar += 1
          taxmin = random.randint(past,yuqori)
          print(f"\n🤖 {urinishlar}-urinish: Men {taxmin} deb o`ylayman.")

          javob = input("Bu to`g`rimi? (ha/katta/kichik):").lower()
     
          if javob == 'ha':
             print(f"🏆 Men {urinishlar} urinishda topdim! Juda qiziqarli bo`ldi! 🎯")
             print("🤖 Men ham aqilli o`yinchiman! 😆")
             break
          elif javob == 'katta':
               yuqori = taxmin - 1
               print("📉 Kichikroq son o`ylayman... 🤔 ")
          elif javob == 'kichik':
               past = taxmin + 1
               print("📈 Kattaroq son o`ylayman... 😏 ")
          else:
               print("❌ Iltimos, faqat 'ha', 'katta' yoki 'kichik' deb javob yozing!")

elif tanlov == '3':
    print("\n🧮 Karra jadvalii mashqlari!")
    togri_javoblar = 0
 
    for i in range(10):
        son1 = random.randint(1, 10)
        son2 = random.randint(1, 10)
        natija = son1 * son2
        javob = int(input(f"{i+1}-savol: {son1} x {son2} ="))

        if javob == natija:
            print("✅ Zo`r! To`g`ri javob!")
            togri_javoblar += 1
        else:
            print(f"❌ Xato! To`g`ri javob: {natija}")

    print(f"\n🏆 Karra jadvali tugadi! Siz {togri_javoblar}/10 savolga to`g`ri javob berdingiz.")

else:
    print("❌ Xato! Iltimos, 1, 2 yoki 3 ni tanlang.")

print("\n🎮 O`yin tugadi! Rahmat, o`yin o`ynaganingiz uchun! 🙌 ")


print("MASHA ALLOH BUGUNGI DARSIM AJOYIB VA MANOLI MAZMUNLI BOLDI")




























































































































