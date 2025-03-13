"""Created on Tue Feb 25 10:46:36 2025

@author: adolat
"""
# Dasturlash asoslari

# 20-dars:FUNKSIYADAN QIYMAT QAYTARISH

# Muallif:Adolat Imomiddinova 

# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return (toliq_ism)

# # talaba = toliq_ism_yasa("abdulaziz","komilov")

# talaba1 = toliq_ism_yasa('abdulaziz','komilov')
# talaba2 = toliq_ism_yasa('komilov','abdulaziz') 
# print(f"Darsga kelgan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")


# def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
#     """Toliq ismi qaytaruvchi funksiya"""
#     if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#        toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# talaba1 = toliq_ism_yasa('abdulaziz','komilov')
# talaba2 = toliq_ism_yasa('komilov','abdulaziz','sobirovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1,avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#        narh = avto['narh']
#     else:
#        narh = "Noma`lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


# AMALIYOT

# teskari so`z yasovchi dastur:
# def reverse_word(word):
#     if word:
#          return f"Natija:{word[::-1]}"
#     else:
#          return "Siz hech narsa kiritmadingiz!"

# info = input("So`zni kiriting:")
# result = reverse_word(info)
# print(result)

# Sonni g`alati tarzda o`zgartiruvchi dastur:
# def kopaytirish():
#     try:
#       num = int(input("Sonni kiriting:")) # Foydalanuvchidan son kirtishini so`raymiz
#       if num < 0:
#          print(f"Musbat korinishi: {abs(num)}") # Manfiy sonni musbat korinishida chiqaramiz
#       else:
#           natija = num * 2
#           print(f"Ko`paytirilgan natija: {natija}")
#     except ValueError:
#           print("Iltimos butun son kiriting!")

# 2-usuli:::

    # def modify_number(num):
#     if num < 0:
#        return f"Musbat ko`rinishi: {abs(num)}"
#     else:
#        return f"Ko`patirilgan natija: {num * 2}"

# info = int(input("Sonni kiritng:"))
# result = modify_number(info)
# print(result)

# So`zni  shifrlovchi dastur
# def encrypt_word(word):
#     if word:
#          return f"SHifrlangan so`z: {'-'.join(str(ord(char)) for char in word)}"
#     else:
#          return "So`z kiritlmadi"

# info = int(input("So`zni kiriting:"))
# result = encrypt_word(info)
# print(result)

# So`zni shiflrovchi dastur
# def encrypt_word(word):
#     if word:
#        return f"SHifrlangan so`z: {'-'.join(str(ord(char)) for char in word)}"
#     else:
#        return "So`z kiritilmadi"

# info = input("So`zni kiritng: ")
# result = encrypt_word(info)
# print(result)

# G`AROYIB MATN O`YIN DASTUR
# def reverse_sentence(sentence):
#     if sentence:
#            return f"Natija: {' '.join(sentence.split()[::-1])}"
#     else:
#            return "Siz matn kiritmadingiz!"

# info = input("Matinni kiritng: ")
# result = reverse_sentence(info)
# print(result)

# SONNI G`ALATI KO`PAYTIRUVCHI DASTUR
def weird_multiply(num):
    if num < 0:
      if num %  2 !=0:
         return f"Juft ko`rinishi: {num + 1}"
      else:
         return f"Musbat ko`rinishi: {abs(num)}"
    else:
       return f"Ko`paytirilgan natija: {num * 3}"

if __name__== "__main__":
    try:
       info = int(input("Sonni kiriting:"))
       result = weird_multiply(info)
       print(result)
except ValueError: 
        print("Xatolik: Son kiritishingiz kerak!")

















