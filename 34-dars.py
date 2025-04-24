#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 08:46:06 2025

@author: adolat
"""
# Dasturlash asoslari

# Muallif: Imomiddinova Adolat: ISOMIDDIN QIZI

# 34-DARS. JSON 

import json
import googlemaps
from apikey import APIKEY

## GoogleMaps
gmaps = googlemaps.Client(key=APIKEY)

data = gmaps.geocode('Olmazor, Toshkent, Uzbekistan')

# print(geocode_result)

g = json.dumps(data[0], indent = 4, sort_keys=True)
print(g)

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m = json.dumps(m)


ism = "adolat"
ism_json = json.dumps(ism)
familiya_json = json.dumps('imomiddinova')


sonlar = ('12','45','23','67')
sonlar_json = json.dumps(sonlar)

bemor = {
   "ism": "Alijon Valiyev",
   "yosh": 30,
   "oila": True,
   "farzandlar": ("Ahmad","Bonu"),
   "allergiya": None,
   "dorilar": [
      {"nomi": "Analgin", "miqdori": 0.5},
      {"nomi": "Panadol", "miqdori": 1.2}
    ]
}

bemor_json = json.dumps(bemor,indent=4)
print(bemor_json)

bemor_json = json.dumps(bemor)
print(bemor_json)

with open('sonlar.json','w') as f:
     json.dump(sonlar,f)

bemor2 = json.loads(bemor_json)

import json

filename = 'bemor.json'
with open(filename) as f:
     bemor = json.load(f)

print(type(bemor))













































