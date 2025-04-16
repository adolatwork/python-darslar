#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 16:20:02 2025

@author: adolat
"""

# Dasturlash asoslari

# 30-DARS. VORISLIK VA POLIFIRIZM

# Muallif: Imomiddinova Adolat: ISOMIDDIN QIZI:

class Shaxs:
   """Shaxslar haqida ma`lumot"""
   def __init__(self,ism,familiya,passport,tyil):
       """Shaxsning xususiyatlari"""
       self.ism = ism
       self.familiya = familiya
       self.passport = passport
       self.tyil = tyil

   def get_info(self):
       """Shaxs haqida ma`lumot"""
       info = f"{self.ism} {self.familiya}."
       info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
       return info

   def get_age(self,yil):
       """Shaxsning yoshini qaytaruvchi metod"""
       return yil - self.tyil

class Talaba(Shaxs):
      """Talaba klassi"""
      def __init__(self ,ism, familiya,passport,tyil):
          """Talabaning xususiyatlari"""
          super().__init__(ism,familiya,passport,tyil)

class Talaba(Shaxs):
     """Talaba klassi"""
     def __init__(self, ism, familiya, passport, tyil, idraqam):
         """Talabaning xususiyatlari"""
         super().__init__(ism, familiya,passport,tyil)
         self.idraqam = idraqam
         self.bosqich = 1

class Talaba(Shaxs):
      """Talaba klassi"""
      def __init__(self, ism, familiya, passport,tyil,idraqam):
          """Talabaning xususiyatlari"""
          super().__init__(ism,familiya,passport,tyil)
          self.idraqam = idraqam
          self.bosqich = 1

      def get_id(self):
          """Talabaning ID raqami"""
          return self.idraqam
 
      def get_bosqich(self):
          """Talabaning o`qish bosqichi"""
          return self.bosqich

      def get_info(self):
          """Talaba haqida ma`lumot"""
          info = f"{self.ism} {self.familiya}."
          info += f"{self.get_bosqich()} - bosqich. ID raqami: {self.idraqam}"
          return info

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuma = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko`rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani,"
        manzil += f"{self.kocha} ko`chasi, {self.uy}-uy"
        return manzil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatalari"""
         super().__init__(ism,familiya,passport,tyil)
         self.idraqam = idraqam
         self.bosqich = 1
         self.manzil = manzil

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o`qish bosqich"""
        return self.bosqich

    def get_info(info):
        """Talabaning haqida ma`lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"











































