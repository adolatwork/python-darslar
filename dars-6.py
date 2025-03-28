#import math

#print(math.ceil(8.7))
#print(math.floor(8.7))


#print(math.sqrt(81))

# ikki xil vaqt kiritiladi
# time1 = soat1, minut1,secund1
# time2 = soat2, minut2, secund2

# soat1 = int(input('1-soat: '))
# minut1 = int(input('1-minut:'))
# secund1 = int(input('1-secund'))

# soat2 = int(input('2-soat:'))
# minut2 = int(input('2-minut:'))
# secund2 = int(input('2-secund:'))

# # 1 soat 3600 secund, 1minut 60 secund
# secund = (soat2-soat1) * 3600 + (minut2-minut1)*60 + (secund2-secund1) 
# print('secund: {}'.format(secund))

# TOPSHIRIQ
# 3 xonali butun son kiritiladi shuni raqamlar yigindisini hisoblab bering 
# u son 685 
# 685  < = INPUT   
# 6 + 8 + 5 = 19

son = int(input("Uch xonli sonni kiriting:"))

# Raqamlarni ajratib olish
birlik = son % 10         # 685 % 10 = 5
onlik = (son // 10) % 10  # (685 // 10) % 10 = 8
yuzlik = son // 100       # 685 // 100 = 6

# Yig`indisini hisoblash
yigindi = birlik + onlik + yuzlik

# Natijani chiqarish
print("{son} => {yuzlik} + {onlik} + {birlik} = {yigindi}")

# ❌









































































