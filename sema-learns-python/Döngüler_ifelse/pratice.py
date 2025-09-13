# Kullanıcı uygun mu

"""X = input("isminizi girin: ")
a = input("eğitim durumunuzu girin: ")
y = int(input("yaşınızı girin: "))

if y<18:
    print(" üzgünüm size ehliyet veremem")
elif a == "lise" or a== "üniversite":
    print("ehliyet alabilirsiniz")
else: 
    print("ehliyet alamazsınız")"""

# hocanın yaptığı versiyon
"""isim=input("isminizi girin: ")
egitim_durumu=input("eğitim durumunuzu girin: ")       
yas=int(input("yaşınızı girin: "))
if (yas>=18) and (egitim_durumu=="lise" or egitim_durumu=="üniversite"):
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")"""
# Bu kod, kullanıcının ismini, eğitim durumunu ve yaşını alır.
# hocanın yaptığı ikinci versiyon
isim=input("isminizi girin: ")
egitim_durumu=input("eğitim durumunuzu girin: ")        
yas=int(input("yaşınızı girin: "))
if (yas>=18):
    if (egitim_durumu=="lise" or egitim_durumu=="üniversite"):
        print("Ehliyet alabilirsiniz")
    else:
        print(f'{isim} Ehliyet alamazsınız eğitim durumunuz uygun değil')
else:
    print(f'{isim}Ehliyet alamazsınız yaşınız uygun değil')
# Bu kod, kullanıcının ismini, eğitim durumunu ve yaşını alır.

"""yazili1 = float(input("1. yazılı notunuzu girin: "))
yazili2 = float(input("2. yazılı notunuzu girin: "))
sozlu = float(input("Sözlü notunuzu girin: "))    
ortalama = (yazili1 + yazili2 + sozlu) / 3

if ortalama >= 85:
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: AA")
elif ortalama >= 70:
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: BB")
elif ortalama >= 50:
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: CC")      
elif ortalama >= 30:    
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: DD")
else:       
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: FF (Kaldınız)")"""

yazili1 = float(input("1. yazılı notunuzu girin: "))
yazili2 = float(input("2. yazılı notunuzu girin: "))
sozlu = float(input("Sözlü notunuzu girin: "))    
ortalama = (yazili1 + yazili2 + sozlu) / 3

if (ortalama >= 85) and (ortalama <= 100):
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: AA")
elif (ortalama >= 70) and (ortalama < 85):
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: BB")
elif (ortalama >= 50) and (ortalama < 70):
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: CC")
elif (ortalama >= 30) and (ortalama < 50):
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: DD")  
elif (ortalama < 30):
    print(f"Ortalamanız: {ortalama:.2f}, Notunuz: FF (Kaldınız)")
else:
    print("Geçersiz not girişi. Lütfen 0-100 arasında bir değer girin.")
# Bu kod, kullanıcının iki yazılı ve bir sözlü notunu alır, 


"""days = int(input("Aracınız kaç gündür trafikte: "))
if days<365:
    print("1.bakım aralığı")
elif days>=365 and days<730:
    print("2.bakım aralığı")

elif days>=730 and days<1095:
    print("3.bakım aralığı")
else:
    print("Trafikteki aracınızın bakım süresi dolmuştur. Lütfen servise götürün.") day time kullanılmadı
# ortalamasını hesaplar ve notunu belirler."""
