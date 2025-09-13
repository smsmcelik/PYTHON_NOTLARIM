#3ün katı olan sayılar
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 3 == 0:
        print(num)
# numbers sayılar toplamı
toplam = 0
for num in numbers:
    toplam +=num #toplam= num+toplam += şeklinde de yazabilirim
    print(toplam)
# numbers sayıların kareleri
for num in numbers:
    print(num ** 2)  

for num in numbers:
    if (num %2 ==1):
        print(num ** 2) #tek sayılar kareleri

citys = ["Ankara", "İstanbul", "İzmir", "Bursa", "Adana", "Gaziantep", "Konya", "Antalya", "Mersin", "Samsun", "rize", "Trabzon"]
for city in citys:
    if (len(city) <=5):
        print(city)

#Ürünlerin fiyat toplamı
products = [
    {"name": "Laptop", "price": 1500},
    {"name": "Telefon", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Kamera", "price": 1200},
]
total_price = 0
for product in products:
    total_price += product["price"]
    print('toplam ürün fiyatı:',total_price)

#fiyatı 1000 den büyük olan ürünler
for product in products:
    if product["price"] > 1000:
        print(f'{product["name"]} fiyatı: {product["price"]} TL')  # Ürün adı ve fiyatı yazdırılır