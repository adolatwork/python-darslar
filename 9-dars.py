# 09-dars.List
# 27-yanvar.2025-yil
# Muallif. Imomiddinova Adolat
# Dasturlash asoslari.

#mevalar = ['olma','anjir','shaftoli','urik']
#narhlar = [12000,19000,10900,23000,25000,36000,-25,43.2]
#sonlar = ['bir','ikki',3,4,5]
#ismlar = []

#Hayvonlar = ['it','mushuk','sigir','qo/`y','quyon','mushuk']
#bozorlik = ['yog`','un','piyoz','banan','go`sht']
#mahsulot = bozorlik.pop(3)
#print('Men' + mahsulot +'sotib oldim')
#print('Olinmagan mahsulotlar:',bozorlik)

# AMALIYOT

# Kiyimlar
kiyimlar = ['Ko\`ylak','SHim','Poyabzal','Qora futbolka']
narhlar = [120_000,150_000,250_000,10_000]

while True:
    print("\nMavjud kiyimlar ro`yxati va narxlari:")
    for i, (kiyim, narh)in enumerate(zip(kiyimlar, narhlar), 1):
        print(f" {i}.{kiyim} - {narh} so`m")

    print("\nTanlov:")
    print("1. Yangi kiyim qo`shish")
    print("2. Kiyim narhini o`zgartirish")
    print("3. Kiyimni ro`yxatdan o`chirish")
    print("4. Barcha kiyimlarni ko`rish")
    print("5. CHiqish")

    tanlov = input("Tanlovni kiriting (1-5): ")

    if tanlov == '1': # Yangi kiyim qo`shish
       yangi_kiyim = input("Yangi kiyim nomini kiriting: ").strip()
    if yangi_kiyim in kiyimlar:
           print("Bu kiyim allaqachon mavjud!")
           continue

       try:
            yangi_narh = int(input(f"{yangi_kiyim} narxini kiriting:"))
       except ValueError:
           print("Narxini faqat raqam bilan kiriting!")
           continue
   
       kiyimlar.append(yangi_kiyim)
       narhlar.append(yangi_narh)
       print(f"{yangi_kiyim} ro`yxatga qo`shildi!")

    elif tanlov == '2': # Kiyim narxini o`zgartirish
       if not kiyimlar:
           print("Ro`yxat bo`sh!")
           continue

       print("\nNarxi o`zgartiriladigan kiyimni tanlang: ")
       for i,kiyim in enumerate(kiyimlar,1):
            print(f"{i}.{kiyim}!")

       try:
           tanlov_index = int(input("Tanlovni kiriting:"))-1
    if tanlov_index < 1 or tanlov_index > len(kiyimlari):
             print("Notug`ri tanlov!")
              continue
           yangi_narh = int(input(f"{kiyimlar[tanlov_index]} yangi narxini kiriting:"))
           narxlar[tanlov_index] = yangi_narx
           print(f"{kiyimlar[tanlov_index]} narx {yangi_narx} so`mga o`zgartirildi")
       except ValueError:
           print("Narxni faqat raqam bilan kiriting")

    elif tanlov == '3': # Kiyimni ro`yxatdan o`chirish
        if not kiyimlar:
            print("Ro`yxat bo`sh!")
            continue

        print("\nO`chiriladigan kiyimni tanlang: ")
        for i, kiyim in enumerate(kiyimlar,1):
            print(f"{i}.{kiyim}")
      
        try:
            tanlov_index = int(input("Tanlovni kiriting:")) - 1
            if tanlov_index < 0 or tanlov_index >= len(kiyimlar):
                print("Notug`ri tanlov!")
                continue
            olingan_kiyim = kiyimlar.pop(tanlov_index)
            narhlar.pop(tanlov_index)
            print(f"{olingan_kiyim} ro`yxatdan o`chiriladi!")
        except ValueError:
            print("Tanlovni faqat raqam bilan kiriting!")
   
    elif tanlov == '4': # Barcha kiyimlarni  ko`rish
      if not kiyimlar:
          print("Ro`yxat bo`sh")
      else:
          print("\nBarcha kiyimlar va narxlari:")
          for kiyim,narh in zip(kiyimlar, narhlar):
              print(f"{kiyim} - {narh} so`m")

    elif tanlov == '5': # CHiqish
         print("Dastur yakunlandi!")
         break
    else:
         print("Notug`ri tanlov! Qayta urinib ko`ring")










































































































