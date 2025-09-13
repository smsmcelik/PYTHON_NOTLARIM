

"""start = int(input("Başlangıç değerini giriniz: "))
end = int(input("Bitiş değerini giriniz: "))    
i = start
while i <= end:  
    i += 1
    if(i % 2 == 1):
        print(i)
#1-100 arasıdaki sayıları geriden yaz
i=100
while i >= 0:
    print(i)
    i -= 1  """

numbers=[]


"""i= 0
while i < 5:
    number = int(input("Lütfen bir sayı giriniz: "))
    numbers.append(number)
    i += 1 

numbers.sort()
print("Girilen sayılar: ", numbers)"""

prodact = []
adet=int(input("Kaç adet ürün gireceksiniz: "))
i = 0
while i < adet:
    product = input("Lütfen ürün adını giriniz: ")
    price = float(input("Lütfen ürün fiyatını giriniz: "))
    prodact.append({"name": product, "price": price })
    i += 1
