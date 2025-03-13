# 08-dars.Sonlar bilan ishlash.
# 24-yanvar. 2025-yil
# Muallif.Adolat
# dasturlash asoslari.

#a = 20
#b = 3,3
#temp = 36.6
#print(type(a))
#aholi_soni = 7_594_376_567
#print("Aholi soni: ",aholi_soni)
#x,y,z = 10,5.5,-56
#c = a*b
#print(c)

#d=100//2
#radius = 20
#PI = 3.14159
#diametr = 2*radius
#print("Aylana uzunligi=",PI* diametr)
#ism = "Abdulaziz"
#yosh = 24
#yosh = str(yosh)
#xabar = ism +' ' +str(yosh)+'yoshda'
#print(xabar)

#t_yil = int(input("Tug'ulgan yilingizni kiriting: "))
#yosh = 2020 - t_yil
#print("Siz",yosh,"yoshda ekansiz")

#a = int("10")
#b = float("10")
#temp = str(36.6)


# AMALIYOT

import math
       
while True:
    # Foydalanuvchidan ismni kiritishni so`rash
    ism = input("Ismingizni kirting: ")
    if not ism:
       print("Ismni kiritish shart! ")
       continue

    # Ismni bosh harfini katta qilish
    ism = ism.title()

    # Yoshingizni kiritish
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
       yosh = int(yosh)
       if yosh <= 0:
          print("Yosh musbat son bo`lishi kerak! ")
          continue
    else:
        print("Yoshni faqat raqam bila kiriting! ")
        continue
    
    # Foydalanuvchiga xabar chiqarish
    xabar = f"Salom, {ism}! Siz {yosh} yoshdasiz."
    print (xabar)

    # Doira radiusini kiritish
    radius = input("Doira radiusini kiriting:")
    try:
         radius = float(radius)
         if radius 










































