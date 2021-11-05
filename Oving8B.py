# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:54:43 2021

@author: Kaan
"""



class Flerevalg:
    def __init__(self, sporsmaal, svaralternativ, verdi):
        self.sporsmaal = sporsmaal
        self.svaralternativ=svaralternativ 
        self.verdi =verdi
        
        
    def __str__(self):
        return f"{self.verdi}: {self.svaralternativ}"        

    def sjekk_svar(self, sjekk):
        if self.verdi==sjekk:
            return f"Alternativ {sjekk} er riktig svar"
        else:
            return f"Alternativ {sjekk} er feil svar"
        






if __name__ =="__main__":
    
    sporsmaal="Hvilket svaralternativ er 2+2?"
    liste1=["1: 16", "2: 3", "3: 4", "4: 5"]
    svar1=Flerevalg(sporsmaal, liste1, "3")
    
    
    sporsmaal2="Hvilket alternativ er hovedstaden til Norge?"
    liste2=["1: Sverige", "2: Oslo", "3: Stavanger", "4: Drammen"]
    svar2=Flerevalg(sporsmaal2, liste2, "2")
    
    sporsmaal3="The best example of viral carcinogenesis in humans is seen with which of the neoplasms?"
    liste3=["1", "2", "3", "4", "5"]
    svar3=Flerevalg(sporsmaal2, liste2, "2")

    sporsmaal4="Myelin is assembled by which type of cell?"
    liste4=["1: Schwann cells", "2: Astrocytes", "3: Neurons", 
            "4: Oligodendrocytes", "5: Mircroglial cells"]
    svar4=Flerevalg(sporsmaal2, liste2, "1" and "4")
    
    print(sporsmaal)
    print("Alternativ 1: 16")
    print("Alternativ 2: 3")
    print("Alternativ 3: 4")
    print("Alternativ 4: 5")
    svar = input("Svar: ")
    print(svar1.sjekk_svar(svar))
    
    print(sporsmaal2)
    print("Alternativ 1: Sverige")
    print("Alternativ 2: Oslo")
    print("Alternativ 3: Stavanger")
    print("Alternativ 4: Drammen")
    svar = input("Svar: ")
    print(svar2.sjekk_svar(svar))

    print(sporsmaal3)
    print("Alternativ 1: Prostatic adenocarcinoma")
    print("Alternativ 2: Melanoma")
    print("Alternativ 3: Cervical cancer")
    print("Alternativ 4: Hepatic angiosarcoma")
    print("Alternativ 5: Retinoblastoma")
    svar = input("Svar: ")
    print(svar3.sjekk_svar(svar))
    
    print(sporsmaal4)
    print("Alternativ 1: Schwann cells")
    print("Alternativ 2: Astrocytes")
    print("Alternativ 3: Neurons")
    print("Alternativ 4: Oligodendrocytes")
    print("Alternativ 5: Mircroglial cells")
    svar = input("Svar: ")
    print(svar4.sjekk_svar(svar))


    for poeng in svar:
        if self.verdi==sjekk:
            poeng =





