
'''
#0-100 Arasında rastgele bir sayı gir.
number= float(input("0-100 arasında bir sayı giriniz: "))

result= (number > 0 and number <=34 100)
print(f'Girilen sayı 0-100 arasında mı? {result}')
'''

"""number = float(input("0-100 arasında bir sayı giriniz: "))
if (number >= 0 ):
    if (number % 2 == 0):
        print(f"{number} sayısı çift sayıdır.") 
    else:
        print(f"{number} sayısı tek sayıdır.")
else:
        print("Girilen sayı negatif.")"""


email = 'smsmcelik@gmail.com'
password = '12345678'   

gemail = input("E-posta adresinizi giriniz: ")
gpassword = input("Şifrenizi giriniz: ")    

if (gemail == email ):
    if (gpassword == password):
        print("Giriş başarılı!")
    else:
        print("Şifre yanlış!")

else:
    print("E-posta yanlış!")


       