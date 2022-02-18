class ElementZamowienia:
    def __init__(self,nazwa,cena,liczbaSztuk):
        self.__cena=cena
        self.__nazwa=nazwa
        self.__liczbaSztuk=liczbaSztuk
    def __str__(self):
        
        tekst=str(self.__nazwa)+" "+str(self.__cena)+" zł "+ str(self.__liczbaSztuk)+" szt. Łącznie:"+ str(self.__cena*self.__liczbaSztuk)+" zł "
        return tekst  

    def obliczRabat(self):
        if self.__liczbaSztuk>=5:
            return 0.9
        else:
            return 1
    def obliczKoszt (self):       
        return self.__cena*self.__liczbaSztuk*self.obliczRabat()
    def obliczCene (self):
        return self.__cena*self.__liczbaSztuk
    
    
    
class Zamowienie ():
    __elementy=[]
    __maksRozmiar=15
    def __init__(self,rozmiar):

        self.__rozmiar=rozmiar

    def dodaj(self, elZam):
        if self.__rozmiar>15:
            return False
        else:
            self.__elementy.append(elZam)
            self.__rozmiar+=1
            
            return True
    def obliczKoszt(self):
        wynikS=0
        for el in self.__elementy:
            wynikS+=el.obliczKoszt()
           
        return wynikS
    def obliczRabaty(self):
        wynikR=0
        for el in self.__elementy:
            wynikR+=el.obliczCene()
        return wynikR-self.obliczKoszt()
    def pisz(self):
        for i in range (len(self.__elementy)):
            print(str(i+1)+". "+ str(self.__elementy[i]))
        print("Całkowity koszt:",self.obliczKoszt())
        print("Naliczony rabat",self.obliczRabaty())
            


z = Zamowienie(10)
z.dodaj(ElementZamowienia("Chleb", 4.0, 2))
z.dodaj(ElementZamowienia("Mleko", 2.5, 1))
z.dodaj(ElementZamowienia("Cukier", 4.0, 5))
z.dodaj(ElementZamowienia("Puszka", 9.0, 1))
z.pisz()
