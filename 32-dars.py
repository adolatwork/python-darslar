#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 10:33:20 2025

@author: adolat
"""
# Dasturlash asoslari

# 32 DARS: OBJECT ORIENTED DASTURLASH 
#          DUNDER METODLARI 2 QISM

# Muallif:Imomiddinova Adolat: ISOMIDDIN QIZI


def __len__(self):
    return len(self.avtolar)

def __getitem__(self,index):
    return self.avtolar[index]

def __setitem__(self,index,qiymat):
    self.avtolar[index]=qiymat

def __call__(self):
    return [avto for avto in self.avtolar]
    
def add_avto(self,*qiymat):
    for avto in qiymat:
        if isinstance(avto,Avto):
            self.avtolar.append(avto)
        else:
            print("Avto kiriting")

salon1 = AvtoSalon("MaxAvto")

avto1 = Avto("GM","Malibu","Qora",2020,40000)











































































































