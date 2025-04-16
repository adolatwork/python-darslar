#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:20:41 2025

@author: adolat
"""

# Dasturlash asoslari

# 31-DARS INKAPSULIYATSIYA VA KLASSGA OID
#         XUSUSIYAT VA METODLAR 

# Muallif: Adolat imomiddinova: ISOMIDDIN QIZI:

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id__ = uuid4()
        Avto.num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.num_avto
    
    def get_km(self):
        return self.__km
  


   

    

    # def get_km(self):
    #     return self.__km

    # def get_id(self):
    #     return self.__id

    # def add_km(self,km):
    #     """Moshinaning km ga yana km qo`shsa bo`ladimi"""
    #     if km>=0:
    #        self.__km += km
    #     else:
    #        print("Moshina km kamaytirib bo`lmaydi")
































































































































































