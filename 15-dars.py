# 13-fevral.2025-yil
# Dasturlash asoslari
# 15-dars:Dictionary {'Lug`at'}
# Muallif:Imomiddinova Adolat
# BISMILLAX ALLOXIM UZING MENGA BUGUNGI DARSIMNI OSON VA MUKAMMAL QILGIN:

# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz ={'apple':'olma', 'apricot':'o`rik', 'banana':'banan'}
# print(en_uz)
# print(en_uz['apple'])

# mevalar = {'olma':10000,'tarvuz':80000,'qovun':10000}
# print(f"Olma narhi {mevalar['olma']} so`m")

# lug`atda istalgan ma`lumot turlarini saqlsh mumkin
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
  # {talaba_0['t_yil']}-yilda tug`ilgan,\
  # {talaba_0['yosh']} yoshda")
# Yangi kalit so`z va qiytma qo`shish
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulaziz'
# print(talaba_0)

# Bo`sh lug`at
# talaba_1 = {}
# talaba_1['ism'] = 'abdulaziz komilov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# Qiymatni yangilash
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#  Kalit so`z qiymatni o`chirib tashlash
# talaba_0 = {'ism':'abdulaziz komilov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)

# Lug`atlarni bir nechta qatorda yozish
# telefonlar = {
     # 'ali':'iphone x',
     # 'abdulaziz':'galaxy s9',
     # 'adolat':'mi 10 pro',
     # 'asmo':'nokia 3310'
      # }

# get()metodi
# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# phone = teleonlar['hasan']
# print(f"Hasanning telefoni {phone}")

# phone = telefonlar.get('ali','Bunday ism majud emas')
# print(phone)

# meva = en_uz.get('apple','Bunday meva mavjud emas')
# print(meva)

# phone = telefonlar.get('hasan')
# print(phone)


# AMALIYOT
# 1.Bo`sh lug`at yaratish
car = {}

# 2.Lug`atga qiymatlar qo`shish
car['model'] = 'Toyota'
car['year'] = 2020
car['color'] = 'black'
car['price'] = 25000

# 3.Lug`atni chop etish
print("Lug`atdagi ma`lumotlar:", car)

# 4.Lug`at ichidan ma`lum kalit bilan qiymat olish 
print("Mashina modeli:", car.get('model'))

# 5.Kalit mavjudligini tekshirish 
if 'color' in car:
    print("Mashina rangi mavjud:", car['color'])

# 6.qiymatni yangilsh
car['price'] = 27000
print("Yangilangan narx:", car['price'])

# 7.Lug`at uzunligin aniqlash
print("Lug`at uzunligi:", len(car))

# 8.Lug`atdagi barcha kalitlarni chiqarish
print("Kalitlar:",list(car.keys()))

# 9.Lug`atdagi barcha qiymatlarni chiqarish
print("Qiymatlar:", list(car.values()))

# 10.Lug`tdagi barcha elementlarni chiqarish
print("Elementlar:", list(car.items()))

# 11.Qiymatni o`chirish
car.pop('color')
print("O`chirilgandan keyin:", car)

# 13.Lug`atdan oxirgi elementni o`chirish
car.popitem()
print("Oxirgi elment o`chirilgandan keyin:", car)

# 14.Lug`atni tozlash
car.clear()
print("Tozlangandan keyin:", car)

# 15.Yangi lug`at yaratish
studen = {
    'name': 'Ali',
    'age': 22,
   'faculty':'Engineering'
}


























































































