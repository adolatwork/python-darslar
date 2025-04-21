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

# data = geocode_result[0]
# kenglik = data['geometry']['loction']['lat']
# uzunlik = data['geometry']['location']['lng']
# print(f"{kenglik},{uzunlik}")




























































































