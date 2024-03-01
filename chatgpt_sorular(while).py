
# Soru 1 : Write a program to print numbers from 1 to 10 using a while loop.

'''
sayı = 0

while True:
    sayı += 1
    print(sayı)
    if sayı == 10:
        print('sayı 10 rakamına ulaştı.')
        break

'''

# Soru 2 : How can you use a while loop to count down from 10 to 1?

'''
sayı = 11

while True:
    sayı -= 1
    print(sayı)
    if sayı == 1:
        print('sayı 1 rakamına ulaştı.')
        break

'''

# Soru 3 : Create a program that prints even numbers from 2 to 20 using a while loop.

'''
sayı = 0

while True:
    sayı += 2
    print(sayı)
    if sayı == 20:
        print('sayı 20 ye ulaştı.')
        break

'''

# Soru 4 : How would you write a program to find the sum of numbers from 1 to 100 using a while loop?

'''
sayı = 0

toplam = 0 

while True:
    sayı += 1            
    toplam += sayı       
    
    print(toplam)
    if sayı == 100:
        print('sayı 100 e ulaştı.')
        break
        
'''

# Soru 5 : Write a program to calculate the factorial of a given number using a while loop.

'''
sayı = 7

faktöriyel = 1

while True:                           
    sayı -= 1                            
    faktöriyel *= sayı                   
    print(sayı)
    if sayı == 2:
        print('sayı 2 ye ulaştı.')
        print(faktöriyel)
        break
        
'''

'''
sayac = 1

carpim = 1

faktöriyel = 1

while True:                                            
    sayac += 1
    faktöriyel *= (sayac*carpim)
    print(sayac)

    if sayac == 10:
        print(f'7 faktöriyelin sonucu : {faktöriyel}')
        break
        
'''

# Soru 6 : Create a program that prints multiples of 5 from 5 to 50 using a while loop.

'''
sayı = 5

carpim = 0

liste = []

while True:
    carpim += 1
    liste.append(sayı*carpim)

    if carpim == 10:
        print(f'5 ten 50 ye kadar 5 in katları olan sayılar şunlardır : {liste}')
        break
        
'''

'''
sayı = 0

while sayı < 50:
    sayı += 5
    print(sayı)

'''

# Soru 7 : How can you use a while loop to print the Fibonacci sequence up to a certain limit?

'''
a = 0                          
b = 1

while a + b < 1000:
    c = a + b
    a = b
    b = c
    print(c)

'''

# Soru 8 : Write a program that prints the squares of numbers from 1 to 10 using a while loop.

'''
sayı= 1

liste = []

while sayı < 11:
    karesi = sayı ** 2
    liste.append(karesi)
    sayı += 1
    
print(liste)

'''

'''
sayı = 1

while sayı < 11:
    karesi = sayı ** 2
    print(karesi)
    sayı += 1

'''

# Soru 9 : Create a program that asks the user for a number and prints its multiplication table using a while loop.

'''
girdi = int(input('bir sayı giriniz : '))

carpim = 1

while girdi < 11:
    sonuc = girdi * carpim
    print(f'{girdi} x {carpim} = {sonuc}')
    carpim += 1

    if carpim > 10:
        break
        
'''

# Soru 10 : How would you implement a program to find the largest number in a series of inputs using a while loop?

'''
a = int(input('bir sayı giriniz : '))
b = int(input('bir sayı giriniz : '))
c = int(input('bir sayı giriniz : '))


while 0 < a < 10 and 0 < b < 10 and 0 < c < 10:
    if a > b and a > c:
        print(f'bu üç sayıdan en büyüğü değeri {a} olan a sayısıdır.')
        break
    
    elif b > a and b > c:
        print(f'bu üç sayıdan en büyüğü değeri {b} olan b sayısıdır.')
        break
    
    elif c > a and c > b:
         print(f'bu üç sayıdan en büyüğü değeri {c} olan c sayısıdır.')
         break

    else:
        print(f'bu üç sayıdan en az ikisi birbirine eşittir.')
        break
        
'''
        
'''
a = int(input('bir sayı giriniz : '))
b = int(input('bir sayı giriniz : '))
c = int(input('bir sayı giriniz : '))
d = int(input('bir sayı giriniz : '))
e = int(input('bir sayı giriniz : '))

liste = []

while a > 0 and b > 0 and c > 0 and d > 0 and e > 0:
      liste.append(a)
      liste.append(b)
      liste.append(c)
      liste.append(d)
      liste.append(e)

      print(f'{max(liste)} listedeki en büyük sayıdır.')
      break
      
'''

'''
sayac = 1

sayılar_listesi = []

while sayac < 10:
    
        girdi = int(input('bir sayı giriniz : '))
        sayılar_listesi.append(girdi)
        sayac += 1

print(sayılar_listesi)
en_büyük_sayı = max(sayılar_listesi)
print(f'{en_büyük_sayı} sayısı liste içindeki en büyük sayıdır.')

'''

# Soru 11 : Write a program to check if a given number is prime using a while loop.

'''
sayac = 2

girdi = int(input('bir sayı giriniz : '))

while True:
    
    if girdi % sayac == 0:
       
       if girdi == sayac:
           print('girilen sayı asaldır.')
           break
       else:
           print('girilen sayı asal değildir.')
           break
    else:
        sayac += 1

'''

# Soru 12 : How can you use a while loop to reverse a given number?

'''
sayı = int(input('sayı giriniz : '))

yenisayi = 0

while sayı > 0:
    kalan = sayı % 10  
    sayı//=10           
    yenisayi = yenisayi*10+kalan     
print(f'ters çevrilmiş sayı : {yenisayi}')

'''

'''
sayı = int(input('bir sayı giriniz : '))

ters_cevrilmis_sayı = 0

while sayı != 0:
    basamak = sayı % 10 
    ters_cevrilmis_sayı = ters_cevrilmis_sayı * 10 + basamak
    sayı //= 10

print(f'ters çevrilmiş sayı : {ters_cevrilmis_sayı}') 

'''

# Soru 13 : Create a program to calculate the average of numbers entered by the user using a while loop.

'''
liste = []

toplam = 0

while True:
    sayı = int(input('bir sayı giriniz : '))
    liste.append(sayı)
    if len(liste) == 5:
        print(liste)
        break

for i in liste:
    toplam += i
print(toplam)

ortalaması = toplam / len(liste)
print(f'liste içindeki sayıların ortalaması : {int(ortalaması)}')

'''

# Soru 14 : How would you implement a program to find the sum of digits of a given number using a while loop?

'''
sayı = int(input('bir sayı giriniz : '))

toplam = 0

liste = []

while sayı != 0:
    kalan = sayı % 10
    liste.append(kalan)
    sayı //= 10
print(liste)

for i in liste:
    toplam += i
print(f'girdiğimiz sayının rakamları toplamı : {toplam}')

'''

# Soru 15 : Create a program to find the LCM (Least Common Multiple) of two numbers using a while loop.

'''
sayı1 = int(input('bir sayı giriniz : '))
sayı2 = int(input('bir sayı giriniz : '))

büyük_sayi = max(sayı1, sayı2)

while True:
    if büyük_sayi % sayı1 == 0 and büyük_sayi % sayı2 == 0:
        ekok = büyük_sayi
        break
    büyük_sayi += 1

print(f"girilen iki sayının ekok'u : {ekok}")

'''

# Soru 16 : Write a program to check if a given number is a palindrome using a while loop.

'''
sayı = int(input('bir sayı giriniz : '))

yenisayı = 0

gecici_sayı = sayı

while gecici_sayı > 0:       
    kalan = gecici_sayı % 10     
    gecici_sayı = (gecici_sayı - kalan) / 10 
    yenisayı = yenisayı * 10 + kalan  

if sayı == yenisayı:
    print('sayı palindromdur.')

else:
    print('sayı palindrom değildir.')

'''

'''
sayı = int(input('bir sayı giriniz : '))

palindrom = ''


while True:
    
    for i in str(sayı):
        palindrom += i
        tersi = palindrom[::-1]
    print(tersi)
    

    if tersi == str(sayı):
        print('bu bir palindrom sayıdır.')
        break

    else:
        print('bu bir palindrom sayı değildir.')
        break
        
'''

# Soru 17 : Create a program to calculate the power of a number using a while loop.

'''
sayı = 1

sayac = 3

while sayac < 10:
    
   üssü =  sayı ** 2
   sayı += 1
   sayac += 1
   print(üssü)

'''

# Soru 18 : reverse a string.

'''
yazı = input('birşeyler yazınız : ')

ters_yazı = ''

index = len(yazı) - 1

while index >= 0:
    
    ters_yazı += yazı[index]

    index -= 1

print('ters çevrilmiş yazı : ', ters_yazı)

'''

# Soru 19 : Multiplication table

'''
rows = 5
cols = 10
i = 1
while i <= rows:
    j = 1
    while j <= cols:
        print(i * j, end="\t")
        j += 1
    print('\n')
    i += 1

'''
# Soru 20 :Find the sum of digits of a number:

'''
sayı = int(input('bir sayı giriniz : '))

toplam = 0 
while sayı > 0:                       
    toplam += sayı % 10              
    sayı //= 10                      
print("rakamlar toplamı:", toplam)

'''

# Soru 21 : Print the first 10 natural numbers in reverse order:

'''
sayı = int(input('bir sayı giriniz : '))

while sayı > 0:
    print(sayı)
    sayı -= 1

'''

# Soru 22 : Print the pattern:

'''
satır = 10

i = 1

while i <= satır:
    print('*' * i, end='\n')
    i += 1

'''

# Soru 23 : Calculate the average of numbers entered by the user:

'''
sayac = 0
toplam = 0
while True:
    sayı = int(input("bir sayı giriniz : "))
    if sayı == 0:
        break
    toplam += sayı
    sayac += 1
if sayac:
    print("ortalama:", toplam / sayac)
else:
    print("girilen sayı yok.")

'''

# Soru 24 : Print the table of a number:

'''
sayı = 50

i = 1

while i <= 30:
    print(sayı, '*', i, '=', sayı * i)
    i += 1

'''

# Soru 25 : Print squares of numbers from 1 to 10:

'''
sayı = int(input('bir sayı giriniz : '))

while 0 < sayı <= 10:
    print(sayı * sayı)
    sayı += 1

'''

# Soru 26 : Print "Hello, World!" 10 times.

'''
kelime = input('bir kelime yazınız : ')

i = 1

while i <= 10:
    print(kelime)
    i += 1

'''

# Soru 27 : Check if a number is present in a given range.

'''
liste = []

while True:

    sayı = int(input('bir sayı giriniz : '))
    
    for i in range(1,100):
        liste.append(i)
        
    if sayı in liste:
        print('girdiğiniz sayı mevcuttur.')
        continue
    else:
        print('girdiğiniz sayı mevcut değildir.')
        break
        
'''

# Soru 28 : Calculate the area of a rectangle.

'''
kısa_kenar = int(input('bir kısa kenar giriniz : '))
uzun_kenar = int(input('bir uzun kenar giriniz : '))

while kısa_kenar < uzun_kenar:

    dikdörtgen_alan = kısa_kenar * uzun_kenar
    print(f'dikdörtgenin alanı :  {dikdörtgen_alan}')
    break
    
'''

# Soru 29 : Calculate the area of a circle.

'''
pi = 3.14

yarıçap = int(input('bir yarıçap giriniz : '))

while yarıçap != 0:
    dairenin_alanı = pi * yarıçap * yarıçap
    print(f'dairenin alanı : {dairenin_alanı}')
    break
    
'''

# Soru 30 : Check if a given number is a perfect square.

'''
sayı = int(input('bir sayı giriniz : '))

while 1 < sayı <= 100:
    if (sayı ** 0.5) % 2 == 0 or (sayı ** 0.5) % 3 == 0 or (sayı ** 0.5) % 5 == 0 or (sayı ** 0.5) % 7 == 0:
        print('bu bir tam karedir.')
        break
    else:
        print('bu bir tam kare değildir.')
        break
        
'''

# Soru 31 : Sort elements of a list in ascending order. Sort elements of a list in descending order.

'''
import random

liste = []

sayac = 1

while sayac < 11:
    liste.append(random.randint(1,100))
    sayac += 1

print(liste)
print()
liste.sort()
print(f'listenin küçükten büyüğe doğru sıralanmış hali : {liste}')
liste.sort(reverse=True)
print(f'listenin büyükten küçüğe doğru sıralanmış hali : {liste}')

'''
# Soru 32 : Sayılar listesini while ile ekrana yazdırın.

'''
sayilar = [1,3,5,7,9,12,19,21]

sayac = 0

while sayac < len(sayilar):
    print(sayilar[sayac])
    sayac += 1

'''

# Soru 33 : Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

'''
basla = int(input('bir sayı giriniz : '))
bitir = int(input('bir sayı giriniz : '))

tek_sayılar = []

while basla < bitir:
    for i in range(basla, bitir+1):
        if i % 2 == 1:
            tek_sayılar.append(i)
    print(tek_sayılar)
    break
    
'''

# Soru 34 : 1 ila 100 arasındaki sayıları azalan şekilde yazdırın.

'''
sayı = 100

while sayı > 0:
    print(sayı)
    sayı -= 1

'''

# Soru 35 : Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

'''
sayılar = []

i = 0

while i < 5:
    sayı = int(input('bir sayı giriniz : '))
    sayılar.append(sayı)
    i += 1
print(sayılar)
sayılar.sort()
print(f'sayıların küçükten büyüğe sıralanmış hali = {sayılar}')

'''

#Soru 36 : Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
           # Ürün sayısını kullanıcıya sorun.
           # Dictionary listesi yapısı (isim, fiyat) şeklinde olsun.
           # Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

'''
ürünler_listesi =[]

i = 0

while i < 5:
    ürün = input('ürün ismini giriniz : ')
    ürünler_listesi.append(ürün)
    i += 1
print(ürünler_listesi)

'''

'''
ürünler_listesi = []

i = 0

adet = int(input('kaç adet ürün eklemek istiyosunuz : '))

while i < adet: 
    ürün_adı = input('ürün adı giriniz : ')
    ürün_fiyatı = int(input('ürün fiyatı giriniz : '))
    ürünler_listesi.append({
        'ürün adı' : ürün_adı,
        'ürün fiyatı' : ürün_fiyatı
        })
    i += 1
print(ürünler_listesi)
print()
print('***********************')

for ürün in ürünler_listesi:
    print(f"ürünün adı : {ürün['ürün adı']}\nürünün fiyatı : {ürün['ürün fiyatı']}\n")

'''

# Soru 37 : Kullanıcıdan alınan 100 ile 200 arasında olan pozitif bir tam sayıyı 0'a kadar geriye doğru azalan şekilde yazınız.
# sayımız 50 ye gelince döngüyü kırma geriye doğru saymaya devam etsin.
# sayımız 10 a gelince döngüyü kır.

'''
sayı = int(input('bir sayı giriniz : '))

if 100 <= sayı <=200:

    while True:
        print(sayı)
        sayı -= 1
        
        if sayı == 50:
            print('sayımız 50 ye ulaştı. döngüye devam ediyoruz..')
            continue

        if sayı == 10:
            print('sayımız 10 a ulaştı döngüyü kırıyoruz...')
            break
else:
    print('lütfen 100 ila 200 arası bir sayı giriniz.')

'''
# Soru 38: Kullanıcıdan alınan n adet sayının toplamını bulan while döngüsü yazınız.

'''
n = int(input('kaç adet sayı girmek istiyosunuz : '))

sayac = 0

toplam = 0

while sayac < n:
    sayı = int(input('bir sayı giriniz : '))
    toplam += sayı
    sayac += 1
print(f"girmiş olduğunuz sayıların toplamı = {toplam}")

'''

# Soru 39: Girilen sayının kaç basamaklı olduğunu bulan while döngüsü yazınız.

'''
sayı = int(input('bir sayı giriniz : '))

sayac = 0

while sayı > 0:
     sayı = sayı // 10
     sayac += 1

print(sayac)

'''

# Soru 40: Girilen sayının basamaklarının toplamını bulan while döngüsü yazınız.

'''
sayı = int(input('bir sayı giriniz : '))

toplam = 0 

while sayı > 0: 
    kalan = sayı % 10 
    toplam += kalan
    sayı = sayı // 10  

print(f"girilen sayının basamakları toplamı = {toplam}")

'''
# Soru 41: Kullanıcıdan alınan n adet sayının toplamını bulan while döngüsünü yazınız.
# Eğer kullanıcının girdiği değer 0 olursa döngüyü bitir girilen sayıların toplamını yazdır.
# Eğer kullanıcının girdiği değer negatif sayı olursa döngüyü kır ve sayıların toplamını yazdırma.

'''
sayı = int(input('bir sayı giriniz : '))

toplam = 0

while sayı != 0:
    if sayı < 0:
        print('negatif sayı girdiniz!!!')
        break
    toplam += sayı
    sayı = int(input('bir sayı daha giriniz : '))

else:
    print(f"girilen sayıların toplamı = {toplam}")

'''
# Soru 42: Kullanıcıdan alınan sayıya kadar olan sayıların karelerini yazan while döngüsünü yazınız.

'''
sayı = int(input('bir sayı giriniz : '))

girilen_sayıların_kareleri = []

while sayı > 0:
    for i in range(1, sayı+1):
        girilen_sayıların_kareleri.append(i**2)
    print(girilen_sayıların_kareleri)
    break
else:
    print('lütfen 0 veya negatif bir sayı girmeyiniz!!')

'''

# Soru 43 : Girilen n sayısına kadar sayıların karelerini yazan while döngüsünü yazınız.

'''
sayı = int(input('bir sayı giriniz : '))

i = 1

while i * i <= sayı:
    print(i * i, end=' ')
    i += 1

'''

# Soru 44: Girilen sayının bütün bölenlerini yazan programı yazınız.

'''
sayı = int(input('bir sayı giriniz : '))

while sayı > 0:
    for i in range(2, sayı):
        if sayı % i == 0:
            print(i)
            i += 1
    break
else:
    print('girilen değer 0 yada 0 dan küçük olamaz..')

'''

# Soru 45: Bir işçi birinci gün x saat çalışıyor, daha sonraki her gün bir önceki güne göre
        #  çalıştığı saat süresini %50 artırıyor. işçi kaçıncı günde en az y saat kadar çalışmış olur.


'''
x = int(input('bir sayı giriniz : '))
y = int(input('bir sayı giriniz : '))

gün_sayısı = 1

while x < y:
    x = x * 1.5
    gün_sayısı += 1

print(gün_sayısı)

'''

# Soru 46: 1 ile 50 arasında bilgisayarın rastgele tuttuğu sayıyı tahmin etmeye
# çalışacağımız bir programı yazalım.
# 0 ile programdan çıkabilirsiniz
# Örneğin;
          # girilen sayı 5 ise daha büyük bir sayı giriniz
          # girilen sayı 7 ise daha küçük bir sayı giriniz
          # girilen sayı 6 ise;
          # sonuç = 6
          # 3 defada buldunuz

'''
import random

rastgele_sayı = random.randint(1,10)

print('0 ile programdan çıkabilirsiniz...')

sayımız = int(input('bir sayı giriniz : '))

sayac = 1

while not(sayımız == 0 or sayımız == rastgele_sayı): 
    if sayımız > rastgele_sayı:
        print('daha küçük sayı giriniz!!')
    
    else:
        print('daha büyük sayı giriniz!!')
    
    sayac += 1

    sayımız = int(input('bir sayı giriniz : '))

if sayımız != 0:
    print(f"{sayac} kerede buldunuz....")

'''

# Soru 47: 3 adet boş liste oluştur. 1 ile 100 arasında rastgele üretilen 10 adet sayıyı bir listeye ekle.
           # Sonra liste içinde döngü yaparak çift sayıları çift sayılar listesine 
           # tek sayıları tek sayılar listesine ekle.

'''
import random

liste = []

ciftler_listesi = []

tekler_listesi = []

sayac = 0

while sayac < 10:
    rastgele_sayı = random.randint(1,100)
    liste.append(rastgele_sayı)
    sayac += 1
print(f'ana listemiz = {liste}')

for i in liste:
    if i % 2 == 0:
        ciftler_listesi.append(i)
        
    else:
        tekler_listesi.append(i)
        
print(f'çiftler listemiz = {ciftler_listesi}')
print(f'tekler listemiz = {tekler_listesi}')

'''
# Soru 48: Count the number of elements in a list.

'''
liste = ['a', 'b', 'c', 12, 40, 55, 86, 'ahmet', 'mehmet']

listedeki_eleman_sayısı = 0
while len(liste) != 0:
    for i in liste:
        print(i, end='  ')
        listedeki_eleman_sayısı += 1
    print(f"\n\n\tlistedeki_eleman_sayısı = {listedeki_eleman_sayısı}")
    break

else:
    print('liste elemanı olmayan boş bir listedir!!')

'''
# Soru 49: Check if a list is empty.

'''
liste = ['a','b','c','d','e']

silinen_eleman_adedi = 0

while len(liste) != 0:
    for i in liste:
        print(liste)
        print(i)
        liste.remove(i)
        silinen_eleman_adedi += 1
        print(liste)
        print(f"silinen_eleman_adedi = {silinen_eleman_adedi}")
        print('****************************************')

    if len(liste) == 0:
        print('listede hiç eleman kalmadı!!!')
        break
else:
    print('başlangıçta listede eleman olması gerek!!!')

'''

# Soru 50: Find the maximum occurring element in a list.

'''
liste1 = ['xyz', 'abcd', 'merhaba', 'ahmet', 'mehmet']

liste2 = []

while len(liste1) != 0:

    for i in liste1:
        liste2.append(len(i))
    

    liste2.sort()
    
    uzunluk = liste2[-1]
    

    for i in liste1:
        if len(i) >= int(uzunluk):
           print(f"liste içindeki en uzun eleman = {i}")
    break
else:
    print('listemizin içinde birden fazla eleman olmak zorunda!!!')

'''
# Soru 51: Find the minimum occurring element in a list.

'''
liste1 = ['ahmet', 'mehmet', 'ali', 'veli', 'hüseyin', 'metin']

liste2 = []

while len(liste1) != 0:
    for i in liste1:
        liste2.append(len(i))

    liste2.sort()
    uzunluk = liste2[0]

    for i in liste1:
        if len(i) <= int(uzunluk):
            print(f"liste içindeki en kısa eleman = {i}")
    break
else:
    print('listemiz boş bir liste olamaz!')

'''

# Soru 52: Find the difference between the largest and smallest element in a list.

'''
liste = []

sayac = 0

while sayac < 10:
    sayı = int(input('bir sayı giriniz : '))
    liste.append(sayı)
    sayac += 1

liste.sort()
print(liste)
en_kücük = liste[0]
en_büyük = liste[-1]

print(f"listedeki en küçük eleman = {en_kücük}")
print(f"listedeki en büyük eleman = {en_büyük}")
print(f"listedeki en büyük eleman ile en küçük elemanın farkı = {en_büyük - en_kücük}")

'''


















        


           

    




                  
                  
            

                
            
            








        








    











        




















        
       












            




        
    











    

























    


        
       




      


    








    
