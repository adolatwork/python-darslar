# 10-dars.LISTS
# 29-yanvar.2025-yil
# Muallif.Imomiddinova_Adolat
# Dasturlash_asoslari
# BISMILLAH....

# TARTIBLASH
# cars = ['bmv','mercedes benz','volvo','general motors','tesla','audi']
# cars.sort()
# # print(cars)

# # # KATTA VA KICHIK HARF
# cars = ['bmv','mercedes benz','volvo','general motors','tesla','audi']
# cars.sort()
# print(cars)

# TESKARI TARTIB
# cars = ['bmv','mercedes benz','volvo','general motors','tesla','audi']
# cars.sort(reverse True)
# print(cars)

# # SOTRED()
# mehmonlar = ['Odil','Hurshid','Temur','Ali','Abdulaziz','Jahongir',]
# print('sotred'()qaytaragan ro`yxat',sorted(mehmonlar))
# print('Asl ro`yxat o`zgarmas qoldi:',mehmonlar)
# print(sorted(mehmonlar,reverseTrue))

# # # SONLI RUYXATLAR
# 


# AMALIYOT
# import random
 
# Tasodifiy sonlardan ro`yxat yaratish
numbers = [1,66,27,54,100,34,50,33,63,4]
print("Asl ro`yxat:",numbers)

# Ro`yxatni tartiblash
numbers.sort()
print("Tartiblangan ro`yxat:",numbers)

# Ro`yxatni teskari tartiblash
numbers.reverse()
print("Yangi tartiblangan ro`yxat:", numbers)

# sorted nomini o`zgartirib, yangi tartiblangan ro`yxat yaratish 
sorted_numbers = sorted(numbers)
print("Yangi tartiblangan ro`yxat:",sorted_numbers)

# Teskari tartiblash
sorted_numbers.reverse()
print("Teskari tartiblangan ro`yxat:", sorted_numbers)

# Ro`yxat ichidagi juft va toq sonlarni aniqlash
juftlar = []
toqlar = []

for num in sorted_numbers:
    if num % 2 == 0:
       juftlar.append(num)
    elif num % 2 == 1:
       toqlar.append(num)
    else:
         print("Noma`lum qiymat aniqlandi:",num)

# Natijani chiqarish
print("\nJuft sonlar:", juftlar)
print("\nToq sonlar:", toqlar)

# Qo`shimcha shart bilan natijani teekshirish
if len(juftlar) > len(toqlar):
    print("\nJuft sonlar koroq ekan!")
elif len(juftlar) < len(toqlar):
     print("\nToq sonlar koproq ekan!")
else:
     print("\nJuft va toq sonlar soni teng")

#  AMALIYOT
# numbers.reverse = [20,200,56,45,55,67,78,6]
# print("Asl ro`yxat:", numbers)























































































































    




































