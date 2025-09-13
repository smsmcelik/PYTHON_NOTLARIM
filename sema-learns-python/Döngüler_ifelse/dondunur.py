import random   

a = random.randint(1, 10)
can=int(input("Kaç canınız olsun: "))
hak = can
dene=0


while hak>0:
    hak -= 1
    dene += 1
    tahmin= int(input("1-10 arasında bir sayı giriniz: "))
    if tahmin == a:
        print(f"Tebrikler {dene}. denemede bildiniz.toplam puanınız: {100-(dene*20)}")
        break
    elif tahmin < a:
        print("Daha büyük bir sayı giriniz.")   
    else:
        print("Daha küçük bir sayı giriniz.")   