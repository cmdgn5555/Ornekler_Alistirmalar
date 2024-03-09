
# Soru 1: Iterate over numbers from 1 to 10 and print each number.

'''
for i in range(1, 10):
    print(i)

'''

# Soru 2: Print "Hello, World!" 10 times using a for loop.

'''
for i in range(1, 11):
    print(f'{i} - hello world')

'''

# Soru 3: Calculate the sum of numbers from 1 to 100 using a for loop.

'''
toplam = 0

for i in range(1, 101):
    toplam += i
print(toplam)

'''

# Soru 4: Print even numbers from 1 to 20 using a for loop.

'''
for i in range(1, 21):
    if i % 2 == 0:
        print(f"1 ila 20 arası çift sayılar = {i}")

'''

# Soru 5: Print odd numbers from 1 to 20 using a for loop.

'''
for i in range(1, 21):
    if i % 2 == 1:
        print(f"1 ila 20 arası tek sayılar = {i}")

'''

# Soru 6: Generate Fibonacci series up to 50 using a for loop.

'''
a = 0
b = 1

for i in range(1,51):
    c = a + b
    print(f"{i}.fibonacci dizisi = {c}")
    a = b
    b = c

'''

# Soru 7: Reverse a given number using a for loop.

'''
sayi = (input('bir sayı giriniz : ')) 
sayinin_tersi = "" 
karakterSayisi = len(sayi)  
for i in range(karakterSayisi): 
    sayinin_tersi += sayi[karakterSayisi - (i+1)]
print(sayinin_tersi)

'''

# Soru 8: Print the factorial of a number using a for loop.

'''
sayi = int(input('bir sayı giriniz : '))

faktöriyel = 1

for i in range(1, sayi+1):
    faktöriyel *= i
print(f"girdiğimiz sayının faktöriyeli = {faktöriyel}")

'''

# Soru 9: Check if a number is prime using a for loop.

'''
sayi = int(input('bir sayı giriniz : '))

if sayi < 0 or sayi == 0:
    print('lütfen 0 dan büyük bir sayı giriniz.')

else:
    for i in range(2, sayi+1):
        if sayi % i == 0:
            if sayi == i:
                print(f"girdiğiniz {sayi} sayısı asal sayıdır.")
                break
                
            else:
                print(f"girdiğiniz {sayi} sayısı asal değildir.")
                break
                
'''

# Soru 10: Calculate the average of numbers input by the user using a for loop.

'''
adet = int(input('kaç adet sayı girmek istiyosunuz : '))

toplam = 0

for i in range(adet):
    sayi = int(input('lütfen bir sayı giriniz : '))
    toplam += sayi
    ortalama = toplam / adet

print(f"girdiğiniz sayıların toplamı = {toplam}")
print(f"girdiğiniz sayıların ortalaması = {int(ortalama)}")

'''

# Soru 11: Print numbers in reverse order from 10 to 1 using a for loop.

'''
for i in range(10, 0, -1):
    print(i)

'''

# Soru 12: Print multiplication table of a given number using a for loop.

'''
sayi = int(input('bir sayı giriniz : '))

for i in range(1, sayi+1):
    print(f"{sayi} x {i} = {sayi * i}")

'''

# Soru 13: Calculate the square of numbers from 1 to 10 using a for loop.

'''
for i in range(1,11):
    print(f"{i} sayısının karesi = {i**2}")

'''

# Soru 14: Print "Yes" if a number is divisible by 3 and 5, otherwise print "No" using a for loop.

'''
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} sayısı üç ve beşe bölünebilir EVET')
        print()
        
    
    else:
        print(f'{i} sayısı üç veya beşe yada her ikisinede bölünemez HAYIR')
        print()

'''

# Soru 15: Calculate the powers of a number using a for loop.

'''
sayi = int(input('bir sayı giriniz : '))

for i in range(1, sayi+1):
    print(f"{sayi} sayısının {i}. kuvveti = {sayi ** i}")
    print()

'''

# Soru 16: Find the largest number among given numbers using a for loop.

'''
liste = [15, 3, 22, 16, 18, 10, 8]

en_buyuk_sayi = liste[0]

for i in liste:
    if en_buyuk_sayi < i:
        en_buyuk_sayi = i
print(en_buyuk_sayi)

'''



# Soru 17: Find the smallest number among given numbers using a for loop.

'''
liste = [5, 8, 12, 15, 20, 23, 28]

en_kucuk_sayi = liste[0]

for i in liste:
    if en_kucuk_sayi > i:
        en_kucuk_sayi == i
print(en_kucuk_sayi)

'''

# Soru 18: Calculate the product of digits of a number using a for loop.

'''
sayı = (input('bir sayı giriniz : '))

carpim = 1

for i in sayı:
    if int(i) != 0: 
        carpim *= int(i)
print(carpim)

'''

# Soru 19: Calculate the GCD of two numbers using a for loop.

'''
def ebob_bul(x, y):
    en_kucuk_sayi = min(x, y)
    en_buyuk_ortak_bolen = 1
    for i in range(1, en_kucuk_sayi+1):
        
        if x % i == 0 and y % i == 0:
            en_buyuk_ortak_bolen = i
    
    print(f"{x} ve {y}'nin en büyük ortak böleni: {en_buyuk_ortak_bolen} sayısıdır!!")

sayi1 = int(input("ilk sayıyı girin : "))
sayi2 = int(input("ikinci sayıyı girin : "))

ebob_bul(sayi1, sayi2)

'''

'''
sayi1 = int(input('ilk sayıyı giriniz : '))
sayi2 = int(input('ikinci sayıyı giriniz : '))

ebob = 0

for i in range(1, sayi1+1): # burda sayi1 yada sayi2 girmemiz farketmez.. sayi2 de girebiirdik..
    if sayi1 % i == 0 and sayi2 % i == 0:
        ebob = i
print(f"{sayi1} ve {sayi2} sayılarının en büyük ortak böleni {ebob} sayısıdır....")

'''

# Soru 20: Find the factorial of a number using recursion using a for loop.

'''
sayi = int(input('bir sayı giriniz : '))

faktöriyel = 1

for i in range(1, sayi+1):
    faktöriyel *= i
print(f"{sayi} sayısının faktöriyeli = {faktöriyel}")

'''

# Soru 21: Check if a given number is palindrome using a for loop.

'''
sayi = int(input('bir sayi giriniz : '))

for i in range(sayi, sayi+1):
    stringe_cevrilen_sayi = str(sayi)
    ters_cevrilen_sayi = stringe_cevrilen_sayi[::-1]

    if stringe_cevrilen_sayi == ters_cevrilen_sayi:
        print('girdiğiniz sayı palindrome bir sayıdır...')
    else:
        print('girdiğiniz sayı palindrome bir sayı değildir!!!')

'''
# 100 ile 200 arasındaki palindrome sayıları for döngüsü ile bulunuz.

'''
for i in range(100, 200):
    string = str(i)
    ters = string[::-1]
    
    if string == ters:
       print(f"100 ile 200 arasındaki palindrome sayılar : {string}")

'''

# Soru 22: Calculate the average of positive numbers input by the user until a negative number is entered using a for loop.

'''
adet = int(input('kaç adet sayı girmek istiyorsunuz : '))

toplam = 0

ortalama = 0

for i in range(adet):
    if adet > 0:
        sayi = int(input('bir sayı giriniz : '))
        if sayi < 0:
            print('sayı negatif olamaz')
        
        else:
            toplam += sayi
            ortalama = toplam / adet
print(int(ortalama))

'''

# Soru 23: Find the square root of a number using a for loop.

'''
karekök = int(input('bir karekök giriniz : '))

for i in range(1,1000):
    deger = karekök ** 0.5
    if deger == i:
       print(f"girdiğiniz karekökün değeri = {deger}")

'''

# Soru 24: Calculate the cube of numbers from 1 to 10 using a for loop.

'''
for i in range(1,10):
    küpler = i**3
    print(küpler)

'''

# Soru 25: Find the sum of squares of first 10 natural numbers using a for loop.

'''
toplam = 0

for i in range(1,11):
    kareler = i ** 2
    toplam += kareler
print(toplam)

'''

# Soru 26: Check if a number is perfect using a for loop.

# kendisi hariç bütün çarpanları toplamı kendisine eşit olan sayılara mükemmel sayı denir.

'''
mükemmel_sayi_kontrol = int(input('bir sayı giriniz : '))

toplam = 0

for i in range(1, mükemmel_sayi_kontrol):  
    if mükemmel_sayi_kontrol % i == 0:
        toplam += i
if toplam == mükemmel_sayi_kontrol:
    print(f"girdiğiniz {mükemmel_sayi_kontrol} sayısı mükemmel sayıdır.")
else:
    print(f"girdiğiniz {mükemmel_sayi_kontrol} sayısı mükemmel sayı değildir.")

'''
# Soru 27: Calculate the sum of digits of a number using a for loop.

'''
sayi = (input('bir sayı girin : '))

toplam = 0

for i in sayi:
    toplam += int(i)
print(toplam)

'''

# Soru 28: Check if a character is vowel or consonant using a for loop.

'''
harf = input('bir harf giriniz : ')

sesli_harfler = 'aeıioöuüAEIİOÖUÜ'

sessiz_harfler = 'bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ'

rakamlar = '0123456789'

for i in harf:
    if len(harf) < 2:
        if i in sesli_harfler:
            print(f"girmiş olduğunuz {i} harfi sesli harftir.")
        
        elif i in rakamlar:
            print('lütfen rakam girmeyiniz!!')
        
        else:
            print(f"girmiş olduğunuz {i} harfi sessiz harftir.")
    else:
        print('lütfen istenen harf olduğu için tek karakter giriniz!!!')
        break
        
'''

# Soru 29 : Calculate the average of numbers in a given list using a for loop.

'''
liste = [10,30,60,100]

toplam = 0

ortalama = 0

for i in liste:
    toplam += i
    ortalama = toplam / len(liste)

print(f"liste içindeki sayıların toplamı = {toplam}")
print(f"liste içindeki sayıların ortalaması = {ortalama}")

'''

# Soru 30: Reverse a list using a for loop.

'''
liste = ['abc', 15, 20.3, 'xyz', 'ali', 'veli', 40, 58.2]

ters_liste = []

for i in range(len(liste)-1, -1, -1): 
    ters_liste.append(liste[i])
print(ters_liste)

'''

# Soru 31: Check if a list is palindrome using a for loop.

'''
liste = [2, 6, 8, 6, 2] 

palindrome_liste = [] 

for i in range(len(liste)-1, -1, -1):
    palindrome_liste.append(liste[i])

if liste == palindrome_liste:
    print(f"{liste} listesi palindrome bir listedir.")

else:
    print(f"{liste} listesi palindrome bir liste değildir!!!")

'''

# Soru 32: Count the number of elements in a list using a for loop.

'''
liste = [12, 20, 35, 40, 'abc', 'xyz', 'hello', 'merhaba']

sayac = 0

for i in liste:
    
    sayac += 1

print(f"liste içindeki eleman sayısı = {sayac}")

'''

# Soru 33: Remove duplicates from a list using a for loop.

'''
liste = ['ev', 'araba', 'uçak', 'gemi', 20, 50, 100, 'uçak', 'gemi', 100, 50]

yeni_liste = []

for i in liste:
    if i not in yeni_liste:
        yeni_liste.append(i)
print(yeni_liste)

'''

# Soru 34: Merge two sorted lists using a for loop.

'''
liste1 = ['a','b','c','selam']

liste2 = [5,10,15,20]

for i in liste1:
    liste2.append(i)
print(liste2)

'''

# Soru 35: Find the intersection of two lists using a for loop.

'''
liste1 = [1,3,8,13,6,18,11,25,28]

liste2 = [2,4,6,8,11,13,17,21,23]

kesisim = []

for i in liste1:
    if i in liste2:
        kesisim.append(i)
print(f"iki listenin kesişimi = {kesisim}")

'''

# Soru 36: Find the union of two lists using a for loop.

'''
liste1 = ['ali', 'veli', 'ahmet', 'mehmet', 100, 200, 300, 400, 500]

liste2 = ['abc', 'ahmet', 'mehmet', 150, 200, 350, 400, 600, 700]

birlesim = []

for i in liste1:
    if i not in liste2:
        birlesim.append(i)

for j in liste2:
    if j not in liste1:
        birlesim.append(j)

print(birlesim)

'''

# Soru 37: Concatenate two lists using a for loop.

'''
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9]

birlestir = []

for i in liste1:
    birlestir.append(i)

for i in liste2:
    birlestir.append(i)

print(birlestir)

'''

# Soru 38: Multiply each element of a list by a given number using a for loop.

'''
sayi = int(input('bir sayı giriniz : '))

liste = [10,15,20,25,30]

carpim_listesi = []

for i in liste:
    carpim_listesi.append(i * sayi)

print(carpim_listesi)

'''

# Soru 39: Check if a list contains a given element using a for loop.

'''
girdi = int(input('bir sayı giriniz : '))

sayılar_listesi = [1,2,5,8,10,12,15,-50,-60,-100]

for i in sayılar_listesi:
    if i == girdi:
        print(f"{girdi} sayısı sayılar listesinde yer almaktadır.")
        break
else:
    print(f"{girdi} sayısı sayılar listesinde mevcut değildir!!!")

'''

'''
kelime = (input('bir kelime giriniz : '))

kelimeler_listesi = ['merhaba', 'python', 'hello', 'selam']

for i in kelimeler_listesi:
    if i == kelime.lower():
        print(f"{kelime} kelimesi kelimeler listesinde yer almaktadır.")
        break
else:
    print(f"{kelime} kelimesi kelimeler listesinde mevcut değildir!!!")

'''

# Soru 40: Remove a specific element from a list using a for loop.

'''
sayi = int(input('bir sayı giriniz : '))

liste = [5,8,13,15,20,23,26]

for i in liste:
    if i == sayi:
        liste.remove(i)
        print(f"{sayi} sayısı listeden kaldırılmıştır!!")
print(liste)

'''

# Soru 41: Find the index of a given element in a list using a for loop.

'''
öge = input('bir kelime giriniz : ')

liste = ['html', 'css', 'python', 'java', 'php', 'c++', 'javascript']

for i in liste:
    if öge == i:
        print(f"girdiğiniz {öge} öğesinin index numarası = {liste.index(öge)}")
        break
else:
    print(f"girdiğiniz {öge} öğesi liste içinde mevcut değil!!!")

'''

# Soru 42: Print the multiplication table of numbers 1 to 5 with a for loop.

'''
sayi = 5

for i in range(1, sayi+1):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
        print('--------------------')

'''

# Soru 43: Print numbers divisible by both 2 and 3 from 1 to 50.

'''
for i in range(1,51):
    if i % 2 == 0 and i % 3 == 0:
       print(f"1'den 50'ye kadar hem 2 hemde 3 e bölünebilen sayılar:\t{i}")

'''

# Soru 44: Print the first 10 perfect squares.

'''
for i in range(1, 11):
    print(f"1 ile 100 arası tam kareler = {i*i}")

'''

# Soru 45: Print the first 10 even Fibonacci numbers.

'''
a = 1
b = 1
c = 2

ilk_10_adet_cift_fibonacci_listesi = []

for i in range(100):
    c = a + b
    a = b
    b = c
    
    if len(ilk_10_adet_cift_fibonacci_listesi) < 10:
        if c % 2 == 0:
            ilk_10_adet_cift_fibonacci_listesi.append(c)

print(ilk_10_adet_cift_fibonacci_listesi)

'''

# Soru 46: Print the first 10 odd Fibonacci numbers.

'''
a = 0
b = 1
c = 0

ilk_10_adet_tek_fibonacci_listesi = []

for i in range(100):
    c = a + b
    a = b
    b = c

    if len(ilk_10_adet_tek_fibonacci_listesi) < 10:
        if c % 2 == 1:
            ilk_10_adet_tek_fibonacci_listesi.append(c)

print(ilk_10_adet_tek_fibonacci_listesi)

'''

'''
for i in range(3):
    for j in range(5):
        print(j)
    print(f"--> {i}")

'''

# Soru 47: 1 den 10 a kadar olan sayılar için çarpım tablosu yazınız.

'''
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={i * j}", end="\t")
    print('')
print('')

print('')

'''


# iç içe for döngüsü alıştırmalar #


'''
liste1 = [5,8,2,5,10,11,17]
liste2 = [4,-2,7,8,12,5]

x = 15

for i in liste1:
    for j in liste2:
        if i + j == x:
            print(f"{i} sayısı ile {j} sayısının toplamı {x} sayısına eşittir.")

'''
'''
sayi = int(input('bir sayı girin : '))

for i in range(1,sayi+1):
    print('*' * i)

'''

'''
sayi = int(input('bir sayı girin : '))

for i in range(sayi):
    print('*' * (sayi - i))

'''

'''
sayi = int(input('bir sayı giriniz : '))

for i in range(1, sayi+1):
    for j in range(i):
        print('*', end=' ')
    print()

'''

'''
sayi = int(input('bir sayı giriniz : '))

for i in range(1, sayi+1):
    for j in range(i):
        print('css', end=' ')
    print()

'''

'''
isimler = ['ali', 'veli', 'ahmet', 'mehmet']

for i in isimler:
    for j in range(1,5):
        print(i*j)
    print()

'''

'''
rakam = [10,20,30,40,50]
harf = ['a','b','c','d','e']

for i in harf:
    for j in rakam:
        print(i, j) 
    print('------')

'''

'''
sayilar = [1,2,3,4]

for i in sayilar:
    for j in sayilar:
        print(f"({i}, {j})")

'''
'''
for i in range(1,6):
    for j in range(1,6):
        print('*' * j, end='\t')
    print()

'''

'''
for k in range(1,10):
    for m in range(k):
        print('*', end='   ')
    print()

for i in range(10, 0, -1):
    for j in range(i):
        print('*', end='   ')
    print()

'''

'''
for i in range(1,5):
    for j in range(1,10):
        print(i*j)
    print()

'''

'''
for i in range(1,5):
    for j in range(1,5):
        print('*', end=' ')
    print()

'''
'''
for i in range(1,5):
    for j in range(i):
        print('*', end=' ')
    print()

'''

'''
satir_say = 4
sutun_say = 4

for satir in range(1, satir_say+1):
    bosluk_say = satir_say - satir
    yıldız_say = sutun_say - bosluk_say

    for bosluk in range(bosluk_say):
        print(' ', end=' ')
    
    for yıldız in range(yıldız_say):
        print('*', end= ' ')
    
    print()

'''

'''
for i in range(4, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

'''

'''
for i in range(1, 5):
    for j in range(i):
        print('*', end=' ')
    print()

for r in range(5, 0, -1):
    for p in range(r):
        print('*', end= ' ')
    print()

'''

'''
for i in range(0, 5):
    for j in range(0, 5 - i):
        print(' ', end= ' ')
    for k in range(0, 2 * i + 1):
        print('*', end=' ')
    print(' ')

'''

'''
for i in range(1, 5):
    for j in range(i):
        print('hello', end=' ')
    print(' ')

for s in range(5, 0, -1):
    for t in range(s):
        print('jack', end=' ')
    print(' ')

'''

'''
sayı1 = int(input('bir sayı giriniz : '))
sayı2 = int(input('bir sayı giriniz : '))
sembol = input('bir sembol giriniz : ')

for x in range(sayı1):
    for y in range(sayı2):
        print(sembol, end=' ')
    print(' ')

'''

'''
liste = []

for i in range(1,5):
    for j in range(i):
        liste.append(j)
print(liste)

'''
'''
meyveler = ['elma', 'armut', 'nar', 'erik', 'portakal']

for i in meyveler:
    for j in range(1,5):
        print(f"{j}-{i}")
    print()

'''







 














    









        
    
    


















    



































    






    










    










    



            
    
   








    



    

        





























        









    










   
    
    

    




        




