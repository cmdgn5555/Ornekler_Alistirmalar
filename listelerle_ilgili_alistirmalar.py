
'''
cars = ['bmw', 'mercedes', 'audi', ['toyota','mazda', 'kia', 'hyundai']]

for i in cars:
    print(i)

print()

print(cars[0])
print()
print(cars[1])
print()
print(cars[2])
print()
print(cars[3])
print()
print(cars[3][0])
print()
print(cars[3][-1])
print()
print(cars[3][-2])

'''

'''
liste = ['P','Y','T','H','O','N']

sayac = 6

for i in liste:
    print(i * sayac)
    sayac -= 1

'''

'''
liste = [27, 32, 36, 41, 49, 53, 56, 60, 68, 77]

cift_sayilar_listesi = []

tek_sayilar_listesi = []

for i in liste:
    if i % 2 == 0:
        cift_sayilar_listesi.append(i)
    if i % 2 == 1:
        tek_sayilar_listesi.append(i)

print(cift_sayilar_listesi)
print(tek_sayilar_listesi)

'''
'''
liste = ['j','a','v','a','s','c','r','i','p','t']

print(liste[::-1])
print(liste[:6])
print(liste[::-2])
print(liste[3:7])
print(liste[4:])

'''

'''
liste1 = ['h','e','l','l','o']
liste2 = ['w','o','r','l','d']

yeni_liste = liste1 + liste2
print(yeni_liste)
print()
print(yeni_liste[-1]*5)
print()
del yeni_liste[2]
print(yeni_liste)
print()
print(len(yeni_liste))
print()
var_mi = 'h' in yeni_liste
print(var_mi)
print()
var_mi_2 = 'j' in yeni_liste
print(var_mi_2)

'''

'''
liste = ['p','y','t','h','o','n']
liste.append('dili')
print(liste)
print()
liste.clear()
print(liste)

'''

'''
sebzeler = ['fasulye', 'bezelye', 'patlıcan', 'kereviz', 'brokoli', 'lahana', 'karnabahar']
sebzeler_2 = sebzeler.copy()
print(sebzeler_2)
'''

'''
liste = ['m','e','r','h','a','b','a','l','a','r']
liste2 = [12,20,25,40,50,40,20,12,12,20,25]

sayı = liste.count('a')
print(sayı)
print()
sayı2 = liste2.count(50)
print(sayı2)

'''

'''
meyveler = ['çilek','şeftali','üzüm','karpuz']
sayılar = [123,9000,102030]

meyveler.extend(sayılar)

print(meyveler)

'''

'''
harfler = ['p','y','t','h','o','n','y','a','z','ı','l','ı','m','p','r','o','g','r','a','m','ı']

sayi = harfler.index('m')

print(sayi)

'''

'''
harfler = ['h','t','l','c','s','b','o','t','s','t','r','p']

harfler.insert(11, 'a')

print(harfler)

'''

'''
rakamlar = [3,7,6,4,9,1,2,8,5]

rakamlar.pop()

print(rakamlar)

rakamlar.pop(3)

print(rakamlar)

'''

'''
yemek = ['i','m','a','m','b','a','y','ı','l','d','ı']

yemek.remove('m')

print(yemek)

yemek.remove('ı')

print(yemek)

yemek.remove('b')

print(yemek)

'''

'''
liste = ['b','i','r','y','a','z','ı','y','a','z','a','l','ı','m']

liste.reverse()

print(liste)

'''

'''
liste = ['p','y','t','h','o','n']

liste.sort()

print(liste)

liste2 = [12, 5, 9, 2, 7, 13, 10]

liste2.sort()

print(liste2)

liste3 = [23, 789393, 4562, 13985, 135, 1956124, 7]

liste3.sort(reverse=True)

print(liste3)

'''

'''
meyveler = ['portakal', 'kivi', 'muz', 'vişne']

meyveler[2] = 'kivi'

meyveler[1] = 'muz'

meyveler[-1] = 'şeftali'

print(meyveler)

'''

'''
cars = ['jeep', 'renault', 'citroen', 'skoda']

del cars[0]

print(cars)

del cars

print(cars)

'''

'''
liste = ['A','B','C','D']

if 'B' in liste:
    print('liste içinde mevcut')
else:
    print('liste içinde mevcut değil!!')

'''

'''
import random

liste = []

sayi = int(input('bir sayı giriniz : '))

for i in range(1, sayi):
    if sayi % i == 0:
        liste.append(random.randint(500,1000))
print(liste)

'''

'''
isimler = ['ali','veli','ahmet','mehmet']
renkler = ['mavi','kırmızı','sarı','siyah']

isim_renk1 = isimler[0] + ' ' + renkler[2]
isim_renk2 = isimler[2] + ' ' + renkler[3]
isim_renk3 = isimler[1] + ' ' + renkler[0]
isim_renk4 = isimler[3] + ' ' + renkler[1]

print(f"{isim_renk1} - {isim_renk2} - {isim_renk3} - {isim_renk4}")

'''
'''
liste = []

adet = int(input('kaç adet sayı eklemek istiyosunuz : '))

for i in range(adet):
    sayi = int(input('sayı giriniz : '))
    liste.append(sayi)
print(liste)

for i in range(adet):
    print(liste[i], end= ' ')

'''

'''
karakter = input('karakter yazınız : ').split('-')

for i in range(len(karakter)):
    karakter[i] = int(karakter[i])

print(karakter)

'''

'''
liste = [int(i) for i in input('bir karakter dizisi giriniz : ').split('-')]

print(liste)

'''

'''
adres = input('bir ip adresi giriniz : ')

b = adres.split('.')

print(b)

'''

'''
adres = input('bir adres giriniz : ')

b = adres.split('.')

print(' '.join(b))

'''

'''
renkler = ['kırmızı', 'siyah', 'mavi', 'pembe', 'turuncu', 'sarı', 'beyaz']

renkler[2:5] = ['blue', 'pink', 'orange']

print(renkler)

'''

'''
liste = [2, 3, 4, 6, 9, 8, 5, 1, 0, 7]

print(liste[1:8:2])

'''

'''
print([1,4,6] * 8)

liste = [34,11,13,7,3,50]
print(min(liste))
print(max(liste))
print(sum(liste))
print(liste.index(50))
print(liste.count(7))

'''

'''
liste = []

print(bool(liste))

'''

'''
import random

liste = [random.randint(1,100) for i in range(6)]

print(liste)

'''


'''
liste = [4, 6, 2, 10, 14, 12, 17]

for i in range(1, len(liste)):
    if liste[i] > liste[i - 1]:
        print(liste[i], end=' ')

'''

'''
liste = [4, 6, 2, 10, 14, 12, 17]

for i in range(1, len(liste)):
    if liste[i - 1] < liste[i]:
        print(liste[i - 1], end=' ')

'''
'''
liste = [6,13,8,15,4,17,9]

maximum = max(liste)

print(maximum, liste.index(maximum))

'''

'''
liste = [32, 13, 5, 11, 17, 20]

minimum = min(liste)

print(minimum, liste.index(minimum))

'''

'''
liste = [54, 32, 85, 100, 22, 45, 101]

maximum_sayi = liste[0]

maximum_sayi_index = 0

for i in range(1, len(liste)):
    if liste[i] > maximum_sayi:
        maximum_sayi = liste[i]
        maximum_sayi_index = i
print(f"maksimum sayımız = {maximum_sayi} ve 
      maksimum sayımızın indeksi = {maximum_sayi_index}")

'''

'''
liste = [35, 46, 23, 14, 20, 52, 13, 58]

minimum_sayi = liste[0]

minimum_sayi_index = 0

for i in range(1, len(liste)):
    if minimum_sayi > liste[i]:
        minimum_sayi = liste[i]
        minimum_sayi_index = i
print(f"minimum sayımız = {minimum_sayi} ve minimum sayımızın indeksi = {minimum_sayi_index}")

'''

'''
liste = [4, 5, 1, 3, 6, 8, 10, 12, 15]

farklı_sayı_adedi = 1
sayıları_eslestirme_adedi = 0

for i in range(1, len(liste)):
    if liste[0] != liste[i]:
        sayıları_eslestirme_adedi += 1
        farklı_sayı_adedi += 1
print(f"listede toplamda {sayıları_eslestirme_adedi} kere eşleştirme yapıldı ve birbirinden farklı {farklı_sayı_adedi} adet sayı tespit edildi...")

'''

'''
liste = [1,1,1,2,2,3,3,3,4,4,4]

sayac = 1

for i in range(len(liste) - 1):
    if liste[i] != liste[i + 1]:
        sayac += 1
print(f"listede birbirinden farklı {sayac} adet sayı vardır!!")

'''

'''
liste = [43, 56, 67, 11, 83, 34, 98, 27, 15]

minimum_sayi = min(liste) # 11

minimum_sayi_index = liste.index(minimum_sayi) # 3

maximum_sayi = max(liste) # 98

maximum_sayi_index = liste.index(maximum_sayi) # 6

liste[minimum_sayi_index] = maximum_sayi

liste[maximum_sayi_index] = minimum_sayi

print(liste)

'''

'''
liste = [10, 20, 30, 40, 50, 60, 70, 80]

silinecek_sayinin_indeksi = int(input('bir indeks no giriniz : '))

for i in range(silinecek_sayinin_indeksi + 1, len(liste)):
             liste[i - 1] = liste[i]
liste.pop()
print(liste)

'''

'''
liste = [10, 20, 30, 40, 50, 60, 70, 80]

silinecek_sayinin_indeksi = int(input('bir indeks no giriniz : '))

for i in range(silinecek_sayinin_indeksi - 1, -1, -1):
             liste[i + 1] = liste[i]
liste.pop(0)
print(liste)

'''

'''
liste = [15,25,35,45,55,65,75,85]

silinecek_sayi_index = int(input('bir indeks no giriniz :  '))

del liste[silinecek_sayi_index]

print(liste)

'''

'''
liste = [50, 100, 150, 200, 250, 300]

index = int(input('bir indeks no giriniz : '))

sayi = int(input('bir sayı giriniz : '))

liste.insert(index, sayi)

print(liste)

'''

'''
renkler = ['sarı', 'turuncu', 'mor', 'siyah', 'yeşil', 'pembe']

for i in enumerate(renkler, 12):
    print(i)

'''














    
    











 





















