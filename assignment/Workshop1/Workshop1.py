import os
clear = lambda:os.system("cls")
clear()

name = 'again'
print(*3*(name,), sep='/')
#*************************************************************** 1.soru
5


#************************************************************************************* 2.soru
    boy = int (input("boyunuzu giriniz (m): "))
kilo = int (input("kilonuzu girini (kg) :"))
    bmi = (kilo*100 / (boy**2)) #BMİ hesaplama
#print("beden kütle indeksiniz: ", (kilo*100 / (boy*boy))) #BMİ hesaplama
print(bmi)
if bmi <= 0.19:
    print ("zayıf kategorisindesiniz")
elif bmi>= 0.20 and bmi <0.249:
    print("normal kilodasınız")
elif bmi >= 0.25 and bmi<0.299:
    print("hafif kilolusunuz")
elif bmi >= 0.30:
        print("Obezsiniz")
#**************************************************** 3.soru
pocket = 200 #dolar
pen = 11 # a pen price
shop = 200 % 11
print(shop)
#**************************************************** 4.soru
sayi4 = int(input("bir sayı giriniz :"))
sayi5 = int(input("bir sayı daha giriniz :"))
print(sayi4, sayi5)
print("{1} {0}".format(sayi4, sayi5))
#**************************************************** 5.soru
x = int(input("x için bir sayı giriniz: ")) # x^2-y^2 hesaplaması
y = int(input("y için bir sayı giriniz: "))
sonuc = x**2 - y**2
print("x^2-y^2 sonucu=", sonuc)

x, y = 5, 4
result = x * x - y * y
print("({} - {}) * ({} + {})) = {}".format(x, y, x, y, result))
#**************************************************** 6.soru
word = " keles "
print(3 * word, sep="/")
#**************************************************** 7.soru
print(True or False) #True
print(False or False) #False
print(True and False) #False
print()