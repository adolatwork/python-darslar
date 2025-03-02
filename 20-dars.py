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
def oraliq(min,max,qadam=None):
    sonlar = []
    while min<max:
      sonlar.append(max)
    if qadam:
        min+=1
    else:
       min+=1
    return sonlar

print(oraliq(1,11,2))
































































































































