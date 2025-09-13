start = int(input("Başlangıç değerini giriniz: "))
end = int(input("Bitiş değerini giriniz: "))    
i = start
while i <= end:
    if i % 2 == 1:  # Sadece tek sayıları yazdır
         i += 1   
        print(i)
            # Her seferinde 1 artır