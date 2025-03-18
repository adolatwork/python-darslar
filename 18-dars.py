# 24-fevral:2025-yil.

# Dasturlash asosari:

# 18-dars: WHILE VA RO`YXATLAR

# Muallif:Adolat Imomiddinova

# print("Yaqin do`slaringizni ro`yxatini tuzamiz.")
# ismlar = []
# n=1 # ismlarni sanash uchun o`zgaruvchi 
# while True:
     # savol = f"{n}-do`stinigizni ismini kiriting:"
     # ism = input(savol)
     # ismlar.append(ism)
     # takrorlash = input("Yana ism qo`shasizmi? (ha/yo`q)")
     # n+=1
     # if takrorlash != 'ha':
        # break


# print("Do`stlaringizni ro`yxati:")
# for ism in ismlar:
    # print(ism.title())


# print("Do`staringizni yoshini saqlaymiz.")
# dostlar = {}
# ishora = True 
# while ishora:
     # ism = input("Do`stingizni ismini kiriting:")
     # yosh = input(f"{ism.title()}ning yoshini kirintg: ")
     # dostlar[ism] = int(yosh)

     # javob = input("Yana ma`lumot qo`shasizmi? (ha\yo`q")
     # if javob == "yo`q":
        # ishora = False


# for ism, yosh in dostlar.items():
    # print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# car = 'lacetti'
# while car in cars:
    # cars.remove(car)

# print(cars)

# talabalar = ['hasan','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
    # talaba = talabalar.pop()
    # baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    # print(f"{talaba.title()} baholandi")
    # baholangan_talabalar[talaba] =int(baho)


# AMALIYOT
import random

# Maxfiy so`zlar ro`yxati
maxfiy_sozlar = ["olma","banan","nok","shaftoli","uzum"]

# O`yin uchun parametrlar
sozlar = []
# xatolar = {}
# ball = 0
# MAX_URINISHLAR = 5

# def oyinni_boshlash():
#     global ball
#     urinishlar = MAX_URINISHLAR
#     maxfiy_soz = random.choice(maxfiy_sozlar)

#     print("\nO`yin boshlandi! Maxfiy sozni topishga harakat qiling.")

#     while urinishlar > 0:
#          kiritilgan_soz = input(f"\nSo`zni kiriting ({urinishlar} urinish qoldi:").strip().lover()

# So`zni ro`yxatga qo`shish
sozlar.append(kiritilgan_soz)

    if kiritigan_soz == maxfiy_soz:
   print("Tabriklayman,siz maxfiy so`zni topdingiz!")
   ball += 1
   break
else:
    urinishlar -= 1
    print("Noto`g`ri! Qayta urinib ko`ring.")

    if urinishlar == 0:
       print(f"Yutqazdingiz! Maxfiy so`z: '{maxfiy_soz}' edi.")

# O`yinni boshlash 
    if __name__=="__main__":
        oyinni_boshlash()




 























































































