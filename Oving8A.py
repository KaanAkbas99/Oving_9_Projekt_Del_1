# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:19:58 2021

@author: Kaan
"""



ordliste=dict()

with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as tekstfil:
    for linjenummer, linje in enumerate(tekstfil):
        #ordene=linje.strip(".")
        ordene=linje.replace(",", " ").replace(".", " ").replace("/", " ")
        #ordene=ordene.replace(":", " ").replace("+", " ").replace("*", " ")
        #ordene=ordene.replace("(", " ").replace(")", " ").replace("=", " ")
        ordene=ordene.split()
        #print(ordene)
        for ordet in ordene:
            ordet=ordet.lower()
            teller=linjenummer+1
            if ordet in ordliste:
                teller=ordliste[ordet]
                ordliste[ordet]=teller
            else:
                ordliste[ordet]=teller         
    for ordet in ordliste:
        print(f"Ordet: {ordet} forkommer i linjenummer: {ordliste[ordet]}")
     
          
    






