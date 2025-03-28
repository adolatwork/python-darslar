# 11-dars:FOR LOOP
# 4-fevral.2025-yil
# Dasturlash asoslari
# Muallif:Adolat

#mehmonlar = ['Ali','Abdulaziz','Mustafo','Imron','Jahongir']
#print('Salom',mehmonlar[0])
#print('Salom',mehmonlar[1])
#print('Salom',mehmonlar[2])
#for mehmon in mehmonlar:
      #print('Salom',mehmon)
      #print('Hayr',mehmon)
#mehmonlar = ['Ali','Abdulaziz','Imron','Jahongir','Mustafo']
#for mehmon in mehmonlar:
    #print('Hurmatli (mehmon),sizni 7 Aprel kuni nohorgi oshga taklif etamiz')
    #print('Hurmat bilan,Paloncheyevlar oilasi\n')
#sonlar = list(range(1,11))
#for son in sonlar:
      #print("(son)ning kvadarati (son**2)ga teng ")
#sonlar = list(range(11))
#sonlar_kvadrati =[]
#for son in sonlar:
    #sonlar_kvadrati.append(son**2)

#print(sonlar)
#print(sonlar_kvadrati)

#dustlar = []
#print("5 ta eng yaqin dustingiz kim")
#for n in range(5):
       #dustlar.append(input(f"(n+1)-dustingizning ismini kiriting"))
#print(dustlar)


# AMALIYOT
# Foydalanuvchidan sonlar orasini kiritishini so`raymiz
start = int(input("Boshlang`ich sonni kiriting:"))
end = int(input("Oxirgi sonni kiriting:"))

# Sonlar ro`yxatini yaratamiz
sonlar = list(range(start,end + 1))

# Natijani chiqarish
print("\n=== Kiritilgan sonlar kvadrati ===\n")

for son in sonlar:
    kvadrat = son ** 2
print(f"{son} ning kvadrati: {kvadrat}")

# Natijani umumlashtirish
print("\n=== Natija tahlili ===\n")

# Barcha kvadartlarni ro`yxat shaklida chiqaramiz
kvadratlar = [son**2 for son in sonlar]
print(f"Barcha kvadratlar: {kvadratlar}")

# Eng kichik kvadratni topamiz
print(f"\nEng kichik kvadrat:{min(kvadratlar)}")
print(f"\nEng katta kvadrat:{max(kvadratlar)}")

# Kvadratlar yig`indisi va o`rtacha qiymtaini chiqaramiz
print(f"\nKvadratlar yig`indisi: {sum(kvadratlar)}")
print(f"Kvadratlarning o`rtacha qiymati: {sum(kvadratlar) / len(kvadratlar):.2f}")

# Dastur tugadi
print("Dastur yakunlandi. Rahmat!")

# ❌









































