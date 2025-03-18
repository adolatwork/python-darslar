# 24-fevral.2025-yil

# Dasturlash asoslari:

# 17-dars:INPUT()VA WHILE

# Muallif:Imomiddinova Adolat


# input()
# ism = input("Ismingiz nima? ")
# savol = f"Salom,{ism.title()}.Yoshingiz nechida?"
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo`yingiz necha metr? ")
# height = float(height)

# while()
# son = 1 # son ga 1 qiymatini beramiz
# while son<5: # toki son 5 dan kichik yoki teng ekan...
    # print(son,end=' ') # son ni konsolga chiqaramiz
    # son += 1 # songa 1 qo`shamiz
    #son  += 1 # songa 1 qo`shamiz 
# print('Dastur tugadi')

# while and input
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting " 
# savol +="(dasturni to`xtatish uchun 'exit' deb yozing):"
# qiymat = ''
# while qiymat !='exit':
   # qiymat = input(savol)
#    if qiymat != 'exit':
      # print(float(qiymat)**2)
# print('Dastur tugadi')


# # ishora
# print("Kiritilgan sonning kvdaratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to`xtatish uchun 'exit' deb yozing):"
# ishora = True
# while ishora:
    # qiymat = input(savol)
    # if qiymat == 'exit':
       # ishora = False
    # else:
       # print(float(qiymat)**2)
# print('Dastur to\`xtadi')


# break while  # break ingliz tilida :SINDIRISH : yoki TUXTATISH DEGAN MANONDA KELADI:
# print("Kirirtilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to\`xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
     # qiymat = input(savol)
     # if qiymat == 'exit':
        # break #tsiklni to`xtatish
     # else:
        # print(float(qiymat)**2)
# print('Dastur tugadi')


# # break for

# sonlar  = list(range(1,11))
# for son in sonlar:
    # if son == 5:
      # break 
    # print(f"{son} ning kvadrati {son**2} ga teng")

# # CONTINUE
# sonlar = list(range(1,11))
# for son in sonlar:
    # if son == 5:
       # continue
    # print(f"{son} ning kvadrati {son**2} ga teng")
  

# # Continue while
# son = 0
# while son<10:
    # son += 1
    # if son%2!=0:
       # continue  
    # else:
      # print(son)



# son = 0
# while son<10:
    # if son%2!=0:
       # continue
    # else:
       # print(son)
    # son += 1



# son = 1
# while son>0:
    # son += 1
    # if son%2!=0:
       # continue    
    # else:     
        # print(son)



# AMALIYOT 
# import random
# Tasodifiy sonlar ro`yxati yaratish
# sonlar = [random.randint(1,20) for _ in range(10)]
# print("Tasodifiy sonlar ro`yxati:", sonlar)
 
# Foydalanuvchi kiritgan sondan boshlash
# son = int(input("Son kiriting:"))

# while True:
#     if son in sonlar:
#          print(f"{son} kvadarati: {son ** 2}")
#          sonlar.remove(son) # Topilgan sonni ro`yxatdan o`chiramiz
    # else:
    #     print(f"{son} ro`yxat yo`q!")
    #     break

# if not sonlar: # Agar barcha sonlar topilsa, dasturni tugatamiz
    # print("Barcha sonlar topildi!")
    # break

# Yangi son kiritishni davom ettirish yoki o`tkazib yuborish 
# son = int(input("Yangi son kiriting (o`tkazish uchun 0):"))
# if son == 0:
#     continue

son = 12

sonlar = [1, 2, 3]

while True:
    if son in sonlar:
        print(f"{son} kvadrati: {son ** 2}")
        sonlar.remove(son) # Topilgan sonni ro`yxatdan o`chiramiz
    else:
        print(f"{son} ro`yxatda yo`q!")
        break

    if not sonlar:
         print("Barcha sonlar topildi!")
         break

son = int(input("Yangi son kiriting (o`tkazish uchun 0):"))
if son == 0:
    pass
else:
    pass
       
    























































