#1-100 e kadar 
x=0
while x<100:
    x+=1
    print(x)
print("Döngü bitti")    

y=1
while y<=100:
    if y%2==0:
        print(y)
    y+=1

a= 1
while a<=100:
    if a%2==1:
        print(f'{a} tek sayıdır')   
    else:
        print(f'{a} çift sayıdır')
    a += 1
  

name='' #false
while not name:  # name boş olduğu sürece döngü devam eder
    name = input("Lütfen adınızı giriniz: ")
print(f"Merhaba {name}!")  # name boş değilse döngüden çıkılır ve selamlaşma yapılırsm