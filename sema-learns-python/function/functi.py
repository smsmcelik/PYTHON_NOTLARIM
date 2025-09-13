def sayHello():
    print("Hello, World!") # bir fonksiyon tanimlama ornegidir sayHello artık bir fonlksiyondur 

sayHello() 
sayHello() 
sayHello() 


def merhabaAd(ad):
    print("Merhaba", ad) # + işareti ile yaparsan bileşik  , yazarsan boşluk bırakır
merhabaAd("Ali")
merhabaAd("Veli") 

def ktsSema(name = "KTS"): #default parametre
    print("Merhaba", name )  

ktsSema('Mustafa')
ktsSema('Sema')
ktsSema() #default parametreyi kullanır


def topla(name ="Sema"):
    return "Merhaba " + name
msg = topla("Ali") #return fonksiyondan bir değer döndürür 
print(msg)  

def çarp(name="Sema"):
    return "Merhaba " + name
msfg = çarp(input("Adınızı giriniz: "))
print(msfg)


def total(num1, num2):
    return num1 + num2  
result = total(10, 20)
print(result)

def kacma(num1, num2):
    return num1 + num2

result = kacma(int(input("Birinci sayıyı girin: ")), int(input("İkinci sayıyı girin: ")))
print("Toplam:", result)


def yasHesapla(dogumYili):
    return 2024 - dogumYili 
ageAli = yasHesapla(1990)
ageVeli = yasHesapla(1985)  
print("Ali'nin yaşı:", ageAli)
print("Veli'nin yaşı:", ageVeli)