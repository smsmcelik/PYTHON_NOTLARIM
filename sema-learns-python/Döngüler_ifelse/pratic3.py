for x in range(10):
    print(x)

numbers = []
for x in range(10):
    numbers.append(x) 

for x in range(10):
    numbers.append(x**2)
numbers = [x**2 for x in range(10)]  # generator expression 
print(numbers)

numbers = [x*x for x in range(10)]
print(numbers) #birded 10 a kadar karelerini yazdırır

numbers= [x*x for x in range(10) if x%3==0] # 3e bölünenlerin karelerini yazdırır
print(numbers)


myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

years = [1990, 1991, 1992, 1993, 1994]
ages = [2024 - year for year in years]
print(ages)

'''results= [x if x % 2 == 0 else "Tek" for x in range(10)] # çift sayıları yazdırır tek olanları tek yazar
print(results)'''
results = []

for x in range (3):
    for y in range(3):
        results.append((x,y))
print(results)  # (0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)