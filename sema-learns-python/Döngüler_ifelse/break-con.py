#break
"""name = "Tural Buse"
for letter in name:
    if letter == "B":
        break
    print(letter) # bu nerede duracağını gösterir"""
"""name= "Sema Tural"
for letter in name:
    if letter == "t":
        continue
    print(letter)  # t harfini atlar ve diğer harfleri yazdırır"""

"""x = 0
while x < 10:       
    x += 1
    if x == 5:
        continue
    print(x)  # 5'i atlar ve diğer sayıları yazdırır
x = 0
while x < 10:       
    x += 1
    if x == 5:
        break
    print(x)  # 5'e gelince döngüyü kırar ve yaz"""


# 1-100 e kadar olan tek sayıların toplamını bul 
a=1
result = 0
while a <= 100:
    result += a
    a += 1
    
print(f'Toplam:{result}')