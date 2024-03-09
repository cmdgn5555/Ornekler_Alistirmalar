
# Soru 1: How do you append an element to the end of a list?

'''
liste = [3, 5, '10', 'elma', 'erik']

öge_ekle = input('bir öğe giriniz : ')

liste.append(öge_ekle)

print(liste)

'''

# Soru 2: How do you insert an element at a specific position in a list?

'''
liste = [3, 5, '10', 'elma', 'erik']

öge_ekle = input('bir öğe giriniz : ')

eklenecek_ögenin_indeksi = int(input('bir indeks no giriniz : '))

liste.insert(eklenecek_ögenin_indeksi, öge_ekle)

print(liste)

'''

# Soru 3: How do you extend a list with another list?

'''
liste1 = [3, 5, '10', 'elma', 'erik']

liste2 = ['python', 'java', 'html', 100, 200]

liste1.extend(liste2)

print(liste1)

'''

# Soru 4: How do you remove the last element from a list?

'''
liste = [3, 5, '10', 'elma', 'erik']

liste.pop()

print(liste)

'''

# Soru 5: How do you remove an element by value from a list?

'''
liste = ['10', 'elma', 'erik', 'mavi', 'mor']

silinecek_öge = input('bir öğe giriniz : ')

liste.remove(silinecek_öge)

print(liste)

'''

# Soru 6: How do you remove an element by index from a list?

'''
liste = [5, 6, 7, 'ev', 'araba', 'arsa', 'otel']

silinecek_ögenin_indeksi = int(input('bir indeks no giriniz : '))

del liste[silinecek_ögenin_indeksi]

print(liste)

'''

# Soru 7: How do you clear all elements from a list?

'''
liste = [10, 15, 'yemek', 'tatlı', 'içecek']

liste.clear()

print(liste)

'''

# Soru 8: How do you check if an element exists in a list?

'''
liste = ['23', '25', '30', 'abc', 'xyz']

girdi = input('bir öğe giriniz : ')

if girdi in liste:
    print('girilen eleman listede mevcut..')

else:
    print('girilen eleman listede mevcut değil!!!!')

'''

# Soru 9: How do you count occurrences of an element in a list?

'''
harfler = ['a','b','c','d','b','b','a','c','d','a','d']

girdi = input('lütfen bir harf giriniz : ')

print(f"girmiş olduğunuz {girdi} harfinin listedeki adedi = {harfler.count(girdi)} tanedir")

'''

# Soru 10: How do you find the index of an element in a list?

'''
liste = ['html', 'css', 'bootstrap', 'java', 'php']

öge = input('bir öge adı giriniz : ')

if öge in liste:
    print(liste.index(öge))

else:
    print('girmiş olduğunuz öğe liste içinde mevcut değildir!!')

'''

# Soru 10: How do you reverse the elements of a list?

'''
adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

for i in range(adet):
    öge = input('bir öğe adı giriniz : ')
    liste.append(öge)

print(liste)
liste.reverse()
print(liste)

'''

'''
liste = [1,2,3,4,5,6,7,8,9,10]

print(liste[::-1])

'''

# Soru 11: How do you sort the elements of a list in ascending order?

'''
liste = [5,2,1,8,4,3,7]

liste.sort()

print(liste)

'''

# Soru 12: How do you sort the elements of a list in descending order?

'''
liste = [9,16,7,11,5,13,4,10]

liste.sort(reverse=True)

print(liste)

'''

# Soru 13: How do you copy a list?

'''
liste = ['havuç', 'turp', 'pırasa', 'limon']

liste2 = liste.copy()

print(liste)
print(liste2)

'''

# Soru 14: How do you iterate over the elements of a list?

'''
liste1 = [10,20,30,40,50,'a','b','c']

for i in liste1:
    print(i*2)

'''

# Soru 15: How do you iterate over the elements of a list with their indices?

'''
liste = ['selam', 'python', 'hello', 'world', 'merhaba']

for i in range(len(liste)):
    print(i, liste[i])

'''

# Soru 16: How do you concatenate two lists?

'''
liste1 = ['a', 'b', 'c', 'd']
liste2 = [1,2,3,4,5]

liste3 = liste1 + liste2

print(liste3)

'''

'''
liste1 = ['a', 'b', 'c', 'd']
liste2 = [1,2,3,4,5]

for i in liste1:
    liste2.append(i)

print(liste2)

'''

# Soru 17: How do you repeat a list a certain number of times?

'''
sayi = int(input('bir sayı giriniz : '))

liste = ['ali', 'veli', 'ismail', 'ibrahim']

print(liste * sayi)

'''

# Soru 18: How do you create a list of unique elements from another list?

'''
liste1 = ['arı', 'sinek', 'yılan', 'timsah', 'sinek', 'yılan', 'arı', 'timsah']

liste2 = []

for i in liste1:
    if i not in liste2:
        liste2.append(i)
print(liste2)

'''
'''
liste1 = [1,4,8,1,2,3,4,8,2,3]

liste2 = []

for i in liste1:
    if i not in liste2:
        liste2.append(i)
print(liste2)

'''

# Soru 19: How do you check if all elements in a list satisfy a condition?

'''
yaslar_listesi = [12, 14, 15, 19, 22, 25, 28]

for i in yaslar_listesi:
    if i > 18:
        print(f'yaşınız {i} , 18 den büyüktür. ehliyet alabilirsiniz..')
    else:
        print(f'yaşınız {i} , 18 den küçüktür. ehliyet alamazsınız.')

'''

# Soru 20: How do you check if any element in a list satisfies a condition?

'''
liste = [17, 23, 32, 35, 41, 49, 55]

for i in liste:
    if i % 2 == 0:
        print(True)
    else:
        print(False)

'''

# Soru 21: How do you filter elements from a list based on a condition?

'''
liste = ['şuraya', 'deneme', 'amaçlı', 'kısa', 'bir', 'yazı', 'yazalım']

for i in liste:
    if len(i) > 5:
        print(i)

'''

# Soru 22: How do you reduce elements of a list to a single value?

'''
liste = [15,20,25,30,35,40,45,50]

for i in range(0, len(liste)-1):
    liste.pop(0)
print(liste)

'''

# Soru 23: How do you join elements of a list into a string?

'''
liste = [1, 'python', 2, 'java', 3, 'html', 4, 'css']

string = '-'.join([str(i) for i in liste])

print(string)

'''

'''
liste = ['istanbul', 'ankara', 'izmir', 'eskişehir', 'bursa', 'adana']

string = ' ... '.join([i for i in liste])

print(string)

'''

'''
liste = [1,2,3,4,5,6,7,8,9]

string = ':'.join([str(i) for i in liste])

print(string)

'''

# Soru 24: How do you split a string into a list?

'''
tel_no = input('bir tel no yazınız : ')

böl = tel_no.split('-')

print(böl)

'''

# Soru 25: How do you convert a list to a tuple?

'''
renkler = ['kırmızı', 'yeşil', 'turuncu', 'sarı', 'beyaz']

demet = tuple(renkler)

print(demet)

'''

# Soru 26: How do you convert a list to a set?

'''
renkler = ['turuncu', 'eflatun', 'yeşil', 'sarı', 'siyah', 'turuncu', 'yeşil', 'sarı', 'eflatun', 'siyah']

küme = set(renkler)

print(küme)

'''

# Soru 27: How do you find the maximum value in a list?

'''
liste = ['p', 'r', 'k', 's', 'y']

maksimum = max(liste)

print(maksimum)

'''
'''
liste = [13, 20, 12, 14, 10, 11, 15]

maximum = max(liste)

print(maximum)

'''

# Soru 28: How do you find the minimum value in a list?

'''
liste = ['g', 'v', 'm', 't', 'r', 'c', 's']

minimum = min(liste)

print(minimum)

'''

'''
liste = [90, 44, 17, 22, 28, 35, 100]

minimum = min(liste)

print(minimum)

'''

# Soru 29: How do you find the sum of all elements in a list?

'''
liste = [12, 34, 50, 53, 67]

toplam = sum(liste)

print(toplam)

'''
'''
liste = ['p','y','t','h','o','n','-','y','a','z','ı','l','ı','m']

topla = ''

for i in liste:
    topla += i

print(topla)

'''

# Soru 30: How do you find the length of a list?

'''
liste = ['hello', 'merhaba', '30', 11, 20, 50]

print(len(liste))

'''

# Soru 31: How do you find the average value of elements in a list?

'''
liste = [2, 4, 6, 8, 10, 12]

toplam = sum(liste)

ortalama = toplam / len(liste)

print(f"liste elemanlarının toplamı = {toplam}")

print(f"liste elemanlarının ortalaması = {ortalama}")

'''

# Soru 32: How do you remove duplicates from a list while preserving order?

'''
liste1 = [1,1,4,4,4,3,3,2,2,2]

liste2 = []

for i in liste1:
    if i not in liste2:
        liste2.append(i)
print(liste2)

'''
'''
liste1 = ['c','b','c','a','b','a'] 

liste2 = []

for i in liste1:
    if i not in liste2:
        liste2.append(i)
print(liste2)

'''

# Soru 33: How do you get the first element of a list if it's not empty?

'''
liste = ['', '', '', 'Python', 'Yazılım']

print('listenin orjinali : ' + str(liste))

sonuc = ' '

for i in liste:
    if len(i) != 0:
        sonuc = i
        break

print('boş olmayan ilk string : ' + str(sonuc))

'''

# Soru 34: How do you get the last element of a list if it's not empty? 

'''
liste = ['nar', 'elma', 'havuç', '', '']

print('listenin orjinali : ' + str(liste))

sonuc = ' '

for i in liste:
     
    if len(i) != 0:
        sonuc = i

print('boş olmayan son string : ' + str(sonuc))

'''
# Soru 35: How do you safely get the nth element of a list with a default value?

'''
liste = [10, 20, 30, 40, 50, 'abc', 'xyz']

n_index = int(input('lütfen bir indeks değeri giriniz : '))

for n_öge in liste:
    n_öge = liste[n_index]

print(f"listenin {n_index+1}. öğesi : {n_öge}")

'''

# Soru 36: How do you check if a list is empty?

'''
liste = []

adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

for i in range(adet):
    öge = input('listeye öge ekleyin : ')
    liste.append(öge)
print(liste)

if len(liste) != 0:
    print('liste boş bir liste değildir..')
else:
    print('liste boş bir listedir!')

'''

# Soru 37: How do you check if two lists are equal?

'''
liste1 = []

liste2 = []

liste1_adet = int(input('liste1 e kaç adet eleman eklemek istiyorsunuz : '))

for i in range(liste1_adet):
    eleman = input('bir eleman giriniz : ')
    liste1.append(eleman)

print(liste1)

liste2_adet = int(input('liste2 ye kaç adet eleman eklemek istiyorsunuz : '))

for j in range(liste2_adet):
    eleman = input('bir eleman giriniz : ')
    liste2.append(eleman)

print(liste2)

if liste1[i] == liste2[j]:
    print('bu iki liste birbirine eşittir..')

else:
    print('bu iki liste birbirine eşit değildir!')

'''

# Soru 38: How do you iterate over a list in batches of a fixed size?

'''
liste = [1,2,3,4,5,6,7,8,9]

print(f"listenin orjinali = {liste}")

for i in range(0, len(liste), 3):
    x = i
    print(liste[x : x + 3])

'''

'''
liste = ['a','b','c','d','x','y','z','w']

print(f"listenin orjinali = {liste}")

for i in range(0, len(liste), 2):
    print(liste[i : i + 3])

'''

'''
liste = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

ters_liste = liste[::-1]

print(f"listenin orjinali = {liste}")

print(f"listenin ters çevrilmiş hali = {ters_liste}")

for i in range(0, len(ters_liste), 5):
    print(ters_liste[i : i + 5])

'''

'''
liste = ['d','l','r','o','w','o','l','l','e','h','m','a','l','e','s','r','e','b','a','n']

ters_liste = liste[::-1]

print(f"listenin orjinali = {liste}")

print(f"listenin ters çevrilmiş hali = {ters_liste}")

for i in range(0, len(ters_liste), 5):
    print(ters_liste[i : i + 5])

'''
'''
liste = ['yazalım', 'birşeyler', 'kısa', 'şuraya']

ters_liste = liste[::-1]


print(f"listenin orjinali = {liste}")

print(f"listenin ters çevrilmiş hali = {ters_liste}")

for i in range(0, len(ters_liste), 2):
    print(ters_liste[i : i + 2])

'''

# Soru 39: How do you swap elements at specific indices in a list?

'''
def konum_degistir(liste, konum_a, konum_b, konum_c, konum_d):
    liste[konum_a], liste[konum_b] = liste[konum_b], liste[konum_a]
    liste[konum_c], liste[konum_d] = liste[konum_d], liste[konum_c]
    
    return liste
    
sayılar_listesi = [5, 3, 9, 7, 8, 6]

print(f"listenin orjinali = {sayılar_listesi}")

print(konum_degistir(sayılar_listesi, konum_a= 0, konum_b= 1, konum_c= 2, konum_d= 5))

'''

'''

liste = ['python', 'html', 'css', 'javascript']

for i in range(len(liste)):
    if len(liste[-1]) > len(liste[i]):
        liste[-1], liste[i] = liste[i], liste[-1]
        
print(liste)

'''

# Soru 40: How do you flatten a list of lists?

'''
iki_boyutlu_liste = [[2,4,6], [1,3,5], [5,10,15], [100,200,300]]

liste = []

for i in iki_boyutlu_liste:
    for j in i:
        liste.append(j)
print(liste)

'''

# Soru 41: How do you zip two lists together?

'''
liste1 = [10,20,30,40,50]
liste2 = ['a','b','c','d','e']

yeni_liste = []

sayac = 0

while sayac < len(liste1) and sayac < len(liste2):

    yeni_liste.append((liste1[sayac], liste2[sayac]))

    sayac += 1

print(yeni_liste)

'''

'''
liste1 = [1,2,3,4]
liste2 = ['python', 'java', 'c++', 'php']

yeni_liste = zip(liste1, liste2)

print(list(yeni_liste))

'''

# Soru 42: How do you unzip a list of tuples into two separate lists?

'''
demet = ((1, 'mavi'), (2, 'turuncu'), (3, 'eflatun'), (4, 'yeşil'))

sayılar_listesi = []

renkler_listesi = []

for i in demet:
    sayılar_listesi.append(i[0])
    renkler_listesi.append(i[-1])

print(sayılar_listesi)
print(renkler_listesi)

'''

# Soru 43: How do you check if a list is sorted in ascending order or in descending order?

'''
liste = [1,2,13,4,15,6,11,10,9,8]

artan_sayac = 0

azalan_sayac = 0

for i in range(0, len(liste) - 1):
    if liste[i] < liste[i + 1]:
       print('liste artan düzende sıralanmıştır..')
       artan_sayac += 1
    
    else:
       print('liste artan düzende sıralanmamıştır!')
       azalan_sayac += 1

print(f"listede artan düzende sıralanan {artan_sayac} adet karşılaştırma yapılmıştır.")
print((f"listede azalan düzende sıralanan {azalan_sayac} adet karşılaştırma yapılmıştır."))

'''

'''
liste = ['abc', 'ab', 'xyz', 'abcd', 'xy', 'x', 'abcde', 'xxyyzz']

artan_sayac = 0

azalan_sayac = 0

for i in range(0, len(liste) - 1):
    if len(liste[i]) < len(liste[i + 1]):
       print('elemanlar artan düzende sıralanmıştır..')
       artan_sayac += 1
    
    else:
       print('elemanlar azalan düzende sıralanmıştır!')
       azalan_sayac += 1

print(f"listede artan düzende sıralanan {artan_sayac} adet karşılaştırma yapılmıştır.")
print((f"listede azalan düzende sıralanan {azalan_sayac} adet karşılaştırma yapılmıştır."))

'''

# Soru 44: How do you find the second largest element in a list?

'''
adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

for i in range(adet):
    sayi = int(input('bir sayı giriniz : '))
    liste.append(sayi)

print(f"listenin orjinal hali = {liste}")

liste.sort()

print(f"listenin küçükten büyüğe sıralanmış hali = {liste}")

print(f"listedeki en büyük ikinci eleman = {liste[-2]}")

'''

'''
adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

uzunluk = []

for i in range(adet):
    eleman = input('lütfen listeye eklenecek bir eleman giriniz : ')
    liste.append(eleman)

print(f"listenin orjinal şekli = {liste}")

liste.sort(key=len)

print(f"liste içindeki elemanların karakter sayısına göre küçükten büyüğe sıralanmış şekli = {liste}")

print(f"liste içindeki elemanlardan karakter sayısına göre en büyük ikinci eleman = {liste[-2]}")

'''


# Soru 45: How do you find the second smallest element in a list?

'''
adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

for i in range(adet):
    sayi = int(input('bir sayı giriniz : '))
    liste.append(sayi)

print(f"listenin orjinal hali = {liste}")

liste.sort(reverse=True)

print(f"listenin büyükten küçüğe sıralanmış hali = {liste}")

print(f"listedeki en küçük ikinci eleman = {liste[-2]}")

'''

'''
adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

for i in range(adet):
    eleman = (input('lütfen listeye eklenecek bir eleman giriniz : '))
    liste.append(eleman)

print(f"listenin orjinal şekli = {liste}")

liste.sort(key=len)

print(f"liste içindeki elemanların karakter sayısına göre küçükten büyüğe sıralanmış şekli = {liste}")

print(f"liste içindeki elemanlardan karakter sayısına göre en küçük ikinci eleman = {liste[1]}")

'''

# Soru 46: How do you find the difference between the largest and smallest elements in a list?

'''
liste = []

adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

for i in range(adet):
    sayi = int(input('lütfen bir sayı giriniz : '))
    liste.append(sayi)

print(f"listenin orjinal sıralanmış şekli = {liste}")

liste.sort()

print(f"listedeki elemanların küçükten büyüğe doğru sıralanmış şekli = {liste}")
print(f"listedeki elemanlar içinde en büyük eleman = {liste[-1]}")
print(f"listedeki elemanlar içinde en küçük eleman = {liste[0]}")
print(f"listedeki elemanlar içinde en büyük eleman ile en küçük elemanın farkı = {liste[-1] - liste[0]}")

'''

'''
liste = []

adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

for i in range(adet):
    eleman = input('lütfen listeye eklenecek elemanı yazınız : ')
    liste.append(eleman)

print(f"listenin orjinal sıralanmış şekli = {liste}")

liste.sort(key=len)

print(f"listedeki elemanların karakter uzunluklarına göre küçükten büyüğe doğru sıralanmış şekli = {liste}")
print(f"listedeki elemanlar içinde karakter uzunluğuna göre en küçük eleman = {liste[0]}")
print(f"listedeki elemanlar içinde karakter uzunluğuna göre en büyük eleman = {liste[-1]}")
print(f"listedeki elemanlar içinde karakter uzunluğuna göre en büyük eleman ile en küçük elemanın farkı = {len(liste[-1]) - len(liste[0])}")

'''

# Soru 47: How do you check if a list contains only unique elements?

'''
liste = [1,6,8,3,2]

print(f"listenin orjinal şekli = {liste}")

durum = False

durum = len(set(liste)) == len(liste)

if durum:
    print('liste benzersiz öğeler içermektedir.')
else:
    print('liste benzersiz öğeler içermemektedir!!!')

'''

# Soru 48: How do you check if a list contains only unique elements?

'''
adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

durum = True

for i in range(adet):
    eleman = input('listeye eklenecek elemanı yazınız : ')
    liste.append(eleman)

print(f"listenin orjinal hali = {liste}")

durum = len(set(liste)) == len(liste)

if durum:
    print('liste benzersiz öğeler içermektedir...')

else:
    print('liste benzersiz öğeler içermemektedir!!!')

'''

# Soru 49: How do you check if a list contains only even numbers?

'''
adet = int(input('listeye kaç adet sayı eklemek istiyorsunuz : '))

liste = []

sayac = 0

for i in range(adet):
    sayi = int(input('bir sayı giriniz : '))
    liste.append(sayi)
    if sayi % 2 == 0:
        sayac += 1

print(f"listemizin orjinal hali = {liste} listemiz içerisindeki çift sayıların adedi = {sayac}")

'''

'''
liste = [2,6,8,10,35,12,14,16]

durum = True


for i in liste:
    if i % 2 != 0:
       durum = False
if durum:
    print('liste içindeki tüm sayılar çifttir.')

else:
    print('liste içindeki sayılardan en az bir tanesi tek sayıdır!!!')

'''

# Soru 50: How do you check if a list contains only odd numbers?

'''
adet = int(input('listeye kaç adet sayı eklemek istiyorsunuz : '))

liste = []

sayac = 0

for i in range(adet):
    sayi = int(input('bir sayı giriniz : '))
    liste.append(sayi)
    if sayi % 2 == 1:
        sayac += 1

print(f"listemizin orjinal hali = {liste} listemiz içerisindeki tek sayıların adedi = {sayac}")

'''

'''
liste = [35,37,43,45,55,59,63,67,4]

durum = True

for i in liste:
    if i % 2 != 1:
        durum = False

if durum:
    print('liste içersindeki tüm sayılar tek sayıdır.')

else:
    print('liste içersindeki sayılardan en az bir tanesi çifttir!!!')

'''

# Soru 51: How do you check if all elements in a list are of the same type?

'''
liste = ['abc','xyz','beta',33]
 
print(f"orjinal liste = {liste}")
 
durum = True

for i in liste:
    if not isinstance(i, type(liste[0])):
        durum = False
        
 
print(f"liste içindeki tüm elemanların tiplerinin aynı olması durumu = {durum}")

'''

'''
liste = [45.3, 22.6, '32', 41.2]

durum = False

sayac = 0 

eleman = liste[0]

for i in liste:
    if type(i) == type(eleman):
        sayac += 1

if sayac == len(liste):
    durum = True

print(f"liste içindeki elemanların tiplerinin aynı olma durumu = {durum}")

'''

# Soru 52: How do you check if all elements in a list are integers?

'''
liste = [12, 15, 20, 'abc', 50.7]

durum = False

sayac = 0


for i in liste:
    if type(i) == int:
        sayac += 1

if sayac == len(liste):
    durum = True

print(f"sayaç = {sayac}")

print(f"liste içindeki tüm elemanların tiplerinin integer olma durumu = {durum}")

'''

# Soru 53: How do you check if all elements in a list are strings?

'''
liste = ['sert', 'kısa', 'uzun']

durum = False

sayac = 0

for i in liste:
    if type(i) == str:
        sayac += 1

if sayac == len(liste):
    durum = True

print(f"sayaç = {sayac}")

print(f"liste içindeki tüm elemanların tiplerinin string olma durumu = {durum}")

'''

# Soru 54: How do you check if all elements in a list are booleans?

'''
liste = [True, False, True, False, 8, 12.5, 'ali']

sayac = 0

durum = False

for i in liste:
    if type(i) == bool:
        sayac += 1

if sayac == len(liste):
    durum = True

print(f"sayaç = {sayac}")

print(f"liste içindeki tüm elemanların tiplerinin boolean olma durumu = {durum}")

'''

# Soru 55: How do you check if all elements in a list are floats?

'''
liste = [12.3, 40.5, 78.9, 'python']

sayac = 0

durum = False

for i in liste:
    if type(i) == float:
        sayac += 1

if sayac == len(liste):
    durum = True

print(f"sayaç = {sayac}")

print(f"liste içindeki tüm elemanların tiplerinin float olma durumu = {durum}")

'''

# Soru 56: How do you check if all elements in a list are negative?

'''
liste = ['-5', -3, -10, -44]

durum = False

sayac = 0

for i in liste:
    if int(i) < 0:
        sayac += 1
    
if sayac == len(liste):
    durum = True

print(f"sayaç = {sayac}")

print(f"liste içindeki tüm elemanların negatif olma durumu = {durum}")

'''

# Soru 57: How do you check if all elements in a list are positive?

'''
liste = [3, 5, 7, 8, 10, 0, '18']

durum = False

sayac = 0

for i in liste:
    if int(i) >= 0:
        sayac += 1

if sayac == len(liste):
    durum = True

print(f"sayaç = {sayac}")

print(f"liste içindeki tüm elemanların pozitif olma durumu = {durum}")

'''

# Soru 58: How do you check if all elements in a list are in a specific range?

'''
liste = [10,15,30,20,25,40]

baslangic = int(input('lütfen bir başlangıç değeri giriniz : '))
bitis = int(input('lütfen bir bitiş değeri giriniz : '))

durum = True

for i in liste:
    if i <= baslangic or i >= bitis:
        durum = False

print(f"değer aralığımız {baslangic} ile {bitis} arasında olmalıdır!!!")

print(f"liste içersindeki tüm elemanların belirlediğimiz aralıkta olması durumu = {durum}")

'''

# Soru 59: How do you find the frequency of each element in a list?

'''
liste = []

adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

for i in range(adet):
    eleman = input('lütfen listeye eleman ekleyiniz : ')
    liste.append(eleman)

print(f"listemizin orjinal hali = {liste}")

for j in liste:
    eleman_sayısı = liste.count(j)

    print(f"listemizdeki eleman {j} adedi ise = {eleman_sayısı}")

'''

'''
liste = [53, 58, 60, 53, 75, 80, 58, 90, 94, 98, 60]

for i in liste:
    sonuc = liste.count(i)
    print(f"liste içindeki elemanımız {i} adedi = {sonuc}")

'''

'''
liste = [1,1,1,1,2,2,2,2,3,3,4,5,5]

eleman_adetleri = []

küme = list(set(liste))

for x in küme:
    eleman_adetleri.append(liste.count(x))


print(f"liste içindeki elemanlarımız : {küme}")
print(f"liste içindeki elemanlarımızın sırasıyla adetleri : {eleman_adetleri}")

'''

'''
adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

for i in range(adet):
    eleman = input('lütfen listeye eleman ekleyiniz : ')
    liste.append(eleman)

print(f"orjinal listemiz = {liste}")
print()

eleman_adetleri = []

küme = list(set(liste))

for j in küme:
    eleman_adetleri.append(liste.count(j))

print(f"listemiz içindeki elemanlar = {küme}")
print()
print(f"listemiz içindeki elemanların sırasıyla adetleri : {eleman_adetleri}")

'''

# Soru 60: How do you remove elements from a list while iterating over it?

'''
liste = [0, 5, 10, True, False, 65.8, 'hello', 'xyz']

print(f"listenin orjinal hali = {liste}")

for i in liste[:]:
    
    liste.remove(i)
print(liste)

'''

# Soru 61: How do you divide a list into two equal parts?

'''
liste = ['limon', 'havuç', 'mandalina', 3, 4, 7, True, False, 38.9, 45.3]

ilk_liste = []

ikinci_liste = []

index = int(input('bir indeks no giriniz : '))

if index == len(liste) / 2:

    ilk_liste = liste[:index]

    ikinci_liste = liste[index:]

else:
    print('lütfen listeyi iki eşit parçaya bölebilmek için liste uzunluğunun yarısına denk gelen bir indeks giriniz!!')


print(f"listenin orjinali = {liste}")
print()
print(f"ilk liste = {ilk_liste}")
print()
print(f"ikinci liste = {ikinci_liste}")

'''

# Soru 62: How do you divide a list into two unequal parts?

'''
liste = ['css', 'html', 'java', 'php', 'python', 1, 2, 3, 4, 5, 6, 7]

ilk_liste = []

ikinci_liste = []

index = int(input('bir indeks no giriniz : '))

if index != len(liste) / 2 and index < len(liste):

    ilk_liste = liste[:index]

    ikinci_liste = liste[index:]
else:
    print('listeyi iki eşit olmayan parçaya bölmek istediğimizden ötürü liste uzunluğunun yarısından farklı bir değerde indeks giriniz!!')
    print('listenin uzunluğuna eşit yada daha fazla bir indeks no giremezsiniz!!!')

print(f"listenin orjinali = {liste}")
print()
print(f"ilk liste = {ilk_liste}")
print()
print(f"ikinci liste = {ikinci_liste}")

'''

# Soru 63: How do you rotate elements of a list to the left or to the right by a certain number of positions?

'''
liste1 = [1,2,3,4,5,6,7,8,9]

print(f"listenin orjinal hali = {liste1}")

liste2 = liste1[5:] + liste1[:5]

print(f"listenin döndürülmüş hali = {liste2}")

'''


'''
liste3 = ['abc', 'xyz', 'python', 'yazılım', 10,20,30,40,50]

print(f"listenin orjinal hali = {liste3}")

liste4 = liste3[4:] + liste3[:4]

print(f"listenin döndürülmüş hali = {liste4}")

'''

'''
liste = ['elma', 'armut', 'erik', 10, 20, 30, 'limon', 'turp', 'havuç', 40, 50, 60]

print(f"listenin orjinal hali = {liste}")

liste2 = liste[6:9] + liste[:3] + liste[3:6] + liste[9:]


print(f"listenin döndürülmüş hali = {liste2}")

'''

# Soru 64: How do you shuffle elements of a list randomly?

'''
import random

adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

liste = []

for i in range(adet):
    eleman = input('listeye eklenecek eleman giriniz : ')
    liste.append(eleman)
print(f"listenin orjinali = {liste}")

random.shuffle(liste)
print()
print(f"listenin rastgele karıştırılmış şekli = {liste}")

'''
'''
import random

liste = ['mercedes', 'toyota', 'renault', 'jaguar', 100, 55555, 2.3, True, False]

print(f"listenin orjinali = {liste}")
print()

random.shuffle(liste)

print(f"listenin rastgele karıştırılmış şekli = {liste}")

'''

# Soru 65: How do you reverse the order of elements in every sublist of a list of lists?

'''
meyveler = [['şeftali', 'kayısı', 'portakal', 'mandalina'],
            ['armut', 'elma', 'erik', 'çilek'],
            ['vişne', 'greyfurt', 'kavun', 'karpuz'],
             ['incir', 'ananas', 'kivi', 'muz']]

yeni_liste = []

for i in meyveler:
    yeni_liste.append(i[::-1])

print(yeni_liste)

'''
'''
liste = [[30,31,32,33,34,35,36], 
         [23,24,25,26,27,28,29],
         [16,17,18,19,20,21,22],
         [9,10,11,12,13,14,15],
         [1,2,3,4,5,6,7,8]]

print(f"listenin orjinali = {liste}")
print()

liste2 = liste[::-1]

print(f"listenin ters çevrilmiş hali = {liste2}")

'''

'''
esyalar = [['dolap', 'ütü', 'fön'],
           ['telefon', 'televizyon', 'klima'],
           ['ütü masası', 'bulaşık makinası', 'çamaşır makinası']]

print(f'eşyalar listesinin orjinali = {esyalar}')
print()

liste = []

for i in esyalar:
    for j in i[::-1]:
        liste.append(j)
print(f"eşyalar listesinin herbir elemanının ters çevrilmiş şeklini tek bir liste haline getirdik = {liste}")

'''

# Soru: users listesi içerisinde bulunan kullanıcılara kurumsal mail adresi oluşturalım.

# örneğin ; burak.yilmaz@bilgeadam.com

# Kullanıcının girdiği passwword is valid mi?

# 1.girilen şifre en az 16 karakter uzunluğunda olmalı

# en az bir büyük bir küçük harf olmalı

# en az bir rakam olmalı

# en az bir tane noktalama işareti olmalı

# her hangi bir ifade tekrar etmemeli

users_list = ['burak yilmaz', 'ertugrul', 'bora eren erdem', 'kerim abdul cabbar okkes']

mail_address = []

birlestirilmis_mail_adresi = []

password_string = ''

password_list = []

password = input('lütfen en az 16 karakter uzunluğunda bir şifre giriniz : ')

büyük_harfler = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'

kücük_harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'

rakamlar = '0123456789'

noktalama_isaretleri = ['.', ',', ';', ':', '...']


for i in users_list:
    
    mail_address.append(i.split(' '))

print(mail_address)


for j in mail_address:
    
    birlestirilmis_mail_adresi.append('.'.join(j) + '@' + 'bilgeadam.com')

print(birlestirilmis_mail_adresi)


if len(password) >= 16:
        for x in password:
           if x in büyük_harfler:
              password_list.append(x)
           elif x in kücük_harfler:
              password_list.append(x)
           elif x in rakamlar:
              password_list.append(x)
           elif x in noktalama_isaretleri:
              password_list.append(x)
           else:
               print('şifre içinde en az bir adet büyük harf, küçük harf, rakam, noktalama işareti olmalı!')
else:
    print('şifre en az 16 karakter uzunluğunda olmalıdır.')
print(password_list)
        
            
       
       













    





























        
































































 























































































