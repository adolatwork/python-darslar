# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Mar 19 09:24:43 2025

# @author: adolat
# """
# # Dasturlash asoslari
# # 23-dars:Modullar
# # Muallif:Adolat Imomiddinova

# def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Sayitimizdagi avtolar ro`yxatini shakillantiramiz.")
# avtolar=[]# salondagi avtolar uchun bo`sh ro`yxat
# while True:
#      print("\nQuyidagi malumotlarni kiriting",end='')
#      kompaniya=input("Ishlab chiqaruvchi: ")
#      model=input("Model: ")
#      rangi=input("Rangi: ")
#      korobka=input("Korobka: ")
#      yili=input("Yili: ")
#      narhi=input("Narhi: ")
#      # Foydalanuvchi kiritgan ma`lumotlardan avto_info yordamida
#      # Lug`at shakillantirib, har bir lug`atni qo`shamiz

# def avto_kirit():
#    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma`lumotlarni

# AMALIYOT
# shop.py
products = {
    1: {"name": "Noutbuk", "price": 800},
    2: {"name": "Smartfon", "price": 500},
    3: {"name": "Quyosh ko`zoynagi","price": 50}
}

def print_info():
    print("\n=== Onlayn do`konimizga xush kelibsiz! ===")
    print("Quyidagi mahsulotlar mavjud:\n")
    for id, product in products.items():
        print(f"{id}. {product['name']} - {product['price']} $")

def get_order():
    order = []
    while True:
         choice = input("\nMahsulot ID kiriting (yoki '0' tugatish uchun):")
         if choice == '0':
            break
         elif choice.isdigit()and int(choice)in products:
              order.append(products[int(choice)])
              print(f"{products[int(choice)]['name']} buyurtmangizga qo`shildi.")
         else:
              print("Noto`g`ri ID! Qayta kiriting.")

    return order
def checout(order):
    total = sum(item["price"] for item in order)
    print("\n=== Buyurtma tasdiqlash ===")
    for item in order:
        print(f"{item['name']} - {item['price']} $")
    print(f"Jami summa: {total} $")

    confirm = input("Tasdiqlash uchun 'ha' deb yozing: ")
    if confirm.lower() == 'ha':
       print("\nBuyurtmangiz qabul qilindi. Rahmat!")
    else:
       print("\nBuyurtmangiz bekor qilindi.")

# main.py
# from shop import print_info, get_order, checkout

def main():
    while True:
       print_info()
       order = get_order()
       if order:
          checkout(order)
       else:
          print("Siz hech qanday mahsulot tanlamadingiz.")

       again = input("\nYana xarid qilasizmi? (ha/yo`q):")
       if again.lower() !='ha':
          print("Do`konimizdan foydalanganingiz uchun katta rahmat!")
          break

if __name__=="__main__":
    main
































































































































































