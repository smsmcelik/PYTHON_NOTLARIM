from datetime import date 
"""a= date.today()
print(a)
print(a.year)
print(a.month)      
print(a.day)
print(a.strftime("%d/%m/%Y"))  # Gün/Ay/Yıl formatında
print(a.weekday())  # Haftanın günü (0=Monday, 6=Sunday)
print(a.isoweekday())  # ISO haftanın günü (1=Monday, 7=Sunday)
"""  # Bu kod, bugünün tarihini alır ve çeşitli tarih bilgilerini gösterir.2
veri=date(int(input("Yıl: ")), 
          int(input("Ay: ")), 
          int(input("Gün: ")))
print(veri)
bugun=date.today()
print(bugun)
fark=bugun-veri
print(f"Aradaki gün sayısı: {fark.days} gün")

"""İf fark.days < 365:
    print("1.bakım aralığı")
elif fark.days < 730:
    print("2.bakım aralığı")    
elif fark.days < 1095:
    print("3.bakım aralığı")
elif fark.days < 1460:
    print("4.bakım aralığı")
else:
    print("doktora götürün")  # Bu kod, kullanıcının girdiği tarihe göre aracın bakım aralığını belirler.
# Bu kod, kullanıcının girdiği tarih ile bugünün tarihi arasındaki farkı"""      
