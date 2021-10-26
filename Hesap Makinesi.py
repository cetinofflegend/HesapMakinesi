print("Basit Hesap Makinesine hoş geldiniz!")

print("Bütün seçenekler görmek için yardım yazınız!")
i = 1

while i == 1:



    secenek = input("Bir seçenek seçin: ")

    if secenek == "carpma":
        sayi1 = input("1. Sayıyı girin: ")
        sayi2 = input("2. Sayıyı girin: ")
        print (int(sayi1) * int(sayi2))
    elif secenek == "toplama":
        sayi1 = input("1: Sayıyı girin: ")
        sayi2 = input("2. Sayıyı girin: ")
        print (int(sayi1) + int(sayi2))
    elif secenek == "yardım":
        print("Tüm  seçenekler: toplama, carpma, çıkarma, bölme, çıkış, yardım")
    elif secenek == "çıkarma":
        sayi1 = input("1. Sayıyı girin: ")
        sayi2 = input("2. Sayıyı girin: ")
        print(int(sayi1) - int(sayi2))
    elif secenek == "bölme":
        sayi1 = input("1. Sayıyı girin: ")
        sayi2 = input("2. Sayıyı girin: ")
        print(int(sayi1) / int(sayi2))
    elif secenek == "çıkış":
        i = 2
        exit

