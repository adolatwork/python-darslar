# 12-dars.TARMOQLANISH
# 4-fevral.2025-yil
# Dasturlash asoslari
# Muallif.Adolat

#avtolar = ['audi','bmv','volvo','kia','hyundai']

#for avto in avtolar:
    #if avto =='bmv':
        #print(avto.apper())
    #else:
        #print(avto.title())

#ism = 'Ali'
#ism.lower()**'ali'

# ism = input('Ismingiz nima?\n>>>')
# if ism.lower()!= 'ali':
    # print(f"*uzr,{ism.title()} biz 'Alini kutayapmiz.")
# else:
    # print("Salom,Ali")

# javob = float(input("12*6 nechiga teng?>>>"))
# if javob!=72:
    # print("Javob xato!")

# yosh = int(input("yoshinigiz nechida?>>>"))
# if yosh>=18:
    # print('Xush kelisz!')
# else:
    # print('Kirish mumkin emas!')

# login = input("Yangi login tanlang")
# if len (login)<=5:
    # print("login 5 harfdan ko`proq bo`lishi shart!")

# yil = int(input("Tug`ulgan yilingizni kiriting:"))
# if 2020-yil<18:
    # print(f"Yoshinigz {2020-yil}da ekan.")
    # print("Kirish mumkun emas!")
# else:
    # print("Xush kelibsz!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65:print("Siz COVID-19 risk guruhida ekansiz")

# x,y = 25,50
# print("x>y")if x>y else print("x>y")




# AMALIYOT

import datetime

# Login funksiyasi
def foydalanuvchi_kirishi():
    print("\n🎯 Xush kelibsiz! Bizning yosh hisoblovchi dasturimizga xush kelibsiz!")
    while True:
        ism = input("🔑 Ismingizni kiriting: ").strip()
        if len(ism) < 6:
           print("🚫 Ism juda oddiy unga kamida 6 ta harf kiriting!")
        elif not ism.isalpha():
           print("🚫 Ism faqat harflardan iborat bo`lishi kerak!")
        else:
           print(f"\n👋 Salom,{ism.capitalize()}!")
           return ism.lower()
 
# Tug`ilgan yilni olish
def tugilgan_yilni_olish():
    hozirgi_yil = datetime.datetime.now().year
    while True:
     try:
          yil = int(input("Tug`ilgan yilingizni kiriting! "))
          if yil > hozirgi_yil:
             print("🚫 Siz hali tug`ilmagansiz, qaytadan kiriting!")
          elif yil < 1900:
             print("🚫 Juda eski yil kiritdingiz, qaytadan urinib ko`ring!")
          else:
             return yil
     except ValueError:
         print("🚫 Iltimos butun son kiritnig!")

# Yoshni hisobblash
def yoshni_hisoblash(yil):
    hozirgi_yil = datetime.datetime.now().year
    yosh = hozirgi_yil - yil
    return yosh

# Motivatsion javob
def motivatsion_javob(yosh):
    if yosh < 10:
       return f"🌟 {yosh} yosh - siz hali juda yoshsiz! Katta imkoniyatlar oldinda!"
    elif yosh < 18:
       return f"🔥 {yosh} yosh - o`qish va rivojlanish davri! Doimo oldinga intiling!"
    elif yosh < 30:
       return f"💪 {yosh} yosh - siz kuchli va g`ayratlisiz! Qat`iyat bilan harakat qiling!"
    elif yosh < 50:
       return f"🧠 {yosh} yosh - tajriba yig`ish va yangi narsalarni o`rganish vaqti!"
    elif yosh < 70:
       return f"🧐 {yosh} yosh - hayotining haqiqiy zavqini his qilish davri!"
    else:
       return f"👑 {yosh} yosh - siz haqiqiy donishmandsiz! Tajribangizni boshqalar bilan ulashing!"

# Foydalanuvchining ismiga asoslangan faktlar
def ism_haqida_faktlar(ism):
    print("\n🧠 Siz haqingizda qiziqarli faktlar:")
    print(f"🔹 Ismingiz uzunligi: {len(ism)} ta belgi.")
    print(f"🔹 Ismingizning birinichi harfi: {ism[0].upper()}.")
    print(f"🔹 Ismingizni bosh harflardan yozsak: {ism.upper()}.")
    print(f"🔹 Ismingizning oxirgi harfi: {ism[-1].upper()}.")

# Tug`ilgan yilingiz haqida faktlar
def yil_haqida_faktlar(yil):
    print("\n📅 Tug`ulgan yilingiz haqida qiziqarli faktlar:")
    print(f"🔸 Tug`ilgan yil juftmi? {'Ha' if yil % 2 == 0 else 'Yo`q'}")
    print(f"🔸 Tug`ilgan yilning kvadrati: {yil ** 2}")
    print(f"🔸 Tug`ilgan yilga 10 qo`shsak: {yil + 10}")

# Yoshni baholash
def yoshni_baholash(yosh):
    print("\n🎯 Yoshingiz asosida tavsiyalar:")
    if yosh < 18:
       print("🚀 O`qish rivojlanishga e`tibor bering!")
    elif yosh < 30:
       print("💼 Karyera qilsh va muvaffaqiyatga erishish vaqti!")
    elif yosh < 50:
       print("🌍 Sayohat qilish va yangi narsalrni kashf qilish vaqti!")
    else:
       print("🍀 HAYOTDAN ZAVQLANING!")

# Foydalanuvchi o`z yoshiga mos maslahat berish
def maslahat_berish(yosh):
    print("🔍 Maslahatlar:")
    for i in range(1, 4):
        if yosh % i == 0:
           print(f"⭐️ Yoshingiz {i} ga bo`linadi!")
        else:
           print(f"❌ Yosh {i} ga bo`linmaydi")

# Foydalanuvchi ishtirokini baholash
def foydalanuvchi_qiziqishlari():
    print("\n🎯 Siz bilan yana gaplashsak bo`ladimi?")
    javob = input("Javob (ha /yo`q: ").lower()
    if javob == "ha":
       print("\n🔥 Ajoyib! Keling davom ettiramiz!")
       asosiy()
    else:
       print("\n👋 Yaxshi, yana ko`rishguncha!")

# Dastur yakuni
def chiqish():
    print("\n✅ Dasturimizdan foydalanganingiz uchun katta rahmat sog` bo`ling!")
    print("\n✅ Yana qaytib keling, do`stim!")

# Asosiy funksiyalar
def asosiy():
    ism = foydalanuvchi_kirishi()
    yil = tugilgan_yilni_olish()
    yosh = yoshni_hisoblash(yil)

    print(f"\n👏 {ism.capitalize()}, siz {yosh} yoshdasiz!")
    print(motivatsion_javob(yosh))

    ism_haqida_faktlar(ism)
    yil_haqida_faktlar(yil)
    yoshni_baholash(yosh)
    maslahat_berish(yosh)

# foydalanuvchi_qiziqishlari()
# chiqish() 



def chiqish():
    print("Dastur yakunlandi. Xayr!")
    # exit()

asosiy()
foydalanuvchi_qiziqishlari()
chiqish()


# Dastur ishga tushadi
# if __name__=="__main__":
#    asosiy()






























































































































































