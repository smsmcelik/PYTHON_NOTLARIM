numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for lis in numbers: #lis numdı lis yaptım çalıştı bir veriliştir istediğini verebilirsin sonradakine liste adı eklenmelidir
    print(lis)

names = ["Ali", "Veli", "Ayşe", "Fatma"]
for name in names:
    print(f'My name is {name}')

name= "Sema Nur Çelik"
for n in name:
    print(n)# Her karakteri ayrı ayrı yazar üstteki küme şeklinde yazmalısın eğer tek tek yazdırmak istiyorsan

tuple=("Ali", "Veli", "Ayşe", "Fatma")
for t in tuple:
    print(f'My name is {t}')

Tural = [(1,2), (3,4), (5,6 ), (7,8)]

for a, b in Tural: 
    print(a,b) #Sadce a yazdımak istersem sadece a yazabilirim kümeler şeklinde yazdırıım 
sema= [(1,2), (3,4), (5,6 ), (7,8)]
for a,b in sema: 
    print(a) #Bu şekilde de yazdırabilirim  tek tek yazar

d={'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}
for item in d:
    print(item) #Bu şekilde de yazdırabilirim  tek tek yazar klar gelir
for item in d.items():
    print(item) #Bu şekilde de yazdırabilirim  klere eşit olan ifadeler gelir 

esma = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}
for key, value in esma.items():
    print(key)
for key, value in esma.items():
    print(value)
for key, value in esma.items():
    print(key, value) #Bu şekilde de yazdırabilirim  tek tek yazar klere eşit olan ifadeler gelir
