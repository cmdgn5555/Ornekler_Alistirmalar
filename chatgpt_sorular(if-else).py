
# Soru 1 : If x is greater than 10, print "x is greater than 10".

'''
x = 15

if x > 10:
    print('x 10 dan büyüktür.')

'''

# Soru 2 : If y is less than 5, print "y is less than 5".

'''
y = 3

if y < 5:
    print('y 5 ten küçüktür.')

'''

# Soru 3 : If a equals b, print "a equals b".

'''
a = 20
b = 20

if a == b:
    print('a b ye eşittir.')

'''

# Soru 4 : If c is not equal to d, print "c is not equal to d".

'''
c = 30
d = 40

if c != d:
    print('c d ye eşit değildir.') 

'''

# Soru 5 : If x is greater than y and x is less than z, print "x is between y and z".

'''
x = 15
y = 10
z = 20

if x > y and x < z:
    print('x, y ile z arasındadır.')

'''

# Soru 6 : If age is less than 18, print "You are a minor".

'''
yas = 17

if yas < 18:
    print('reşit değisiniz.')

'''

# Soru 7 : If temperature is greater than 100, print "It's very hot".

'''
sicaklik = 105

if sicaklik > 100:
    print('çok sıcak')

'''

# Soru 8 : If score is greater than or equal to 90, print "You got an A".

'''
puan = 90

if puan >= 90:
    print('A aldınız.')

'''

# Soru 9 : If the day is Monday or Friday, print "It's the beginning or end of the week".

'''
gün = ['pazartesi', 'salı', 'çarşamba', 'perşembe', 'cuma', 'cumartesi', 'pazar']

for i in gün:
    if i == 'pazartesi':
        print('haftanın başı')
    elif i == 'cuma':
        print('haftanın sonu')

'''

# Soru 10 : If x is not equal to y, print "x is not equal to y".

'''
x = 10
y = 5

if x != y:
    print('x ve y birbirine eşit değildir.')

'''

# Soru 11 : If the color is red, print "The color is red".

'''
renk = 'kırmızı'

if renk == 'kırmızı':
    print('renk kırmızıdır.')

'''

# Soru 12 : If the speed is less than 50, print "Slow down!".

'''
hiz = 49

if hiz < 50:
    print('yavaşla!')

'''

# Soru 13 : If the number is even, print "The number is even".

'''
sayi = 30

if sayi % 2 == 0:
    print('sayı çift sayıdır.')

'''

# Soru 14 : If the result is negative, print "The result is negative".

'''
sayi = -1 

if sayi < 0:
    print('sayı negatiftir.')

'''

# Soru 15 : If the user input is 'yes', print "User confirmed".

'''
kullanıcı_girisi = 'evet'

if kullanıcı_girisi == 'evet':
    print('kullanıcı onaylı.')

'''

# Soru 16 : If the file exists, print "File found".

'''
girdi = input('dosya ismini giriniz : ')

dosyalar_listesi = ['abc.jpg']

for i in dosyalar_listesi:
    if i == girdi:
        print('dosya bulundu.')
  
    else:
        print('böyle bir dosya yok.')

'''

# Soru 17 : If the balance is zero, print "Account is empty".

'''
bakiye = 0

if bakiye == 0:
    print('hesap boş.')

'''

# Soru 18 : If the password is correct, print "Access granted".

'''
girdi = int(input('bir şifre giriniz : '))

sifre = 123456789

if sifre == girdi:
    print('erişim izni verildi.')

else:
    print('erişim izni reddedildi.')

'''

# Soru 19 : If the value is within the range of 1 to 10, print "Value is in range".

'''
deger = 5

for i in range(1,10):
    if deger == i:
        print('değer bu aralıktadır.')

'''

# Soru 20 : If the day is Sunday, print "It's a weekend".

'''
girdi = input('bir gün ismi yazınız : ')

günler = ['cumartesi', 'pazar']

for i in günler:
    if i == girdi:
        print('bugün haftasonudur.')
    
    elif i == girdi:
        print('bugün haftasonudur.')

'''

# Soru 21 : If the temperature is below freezing, print "It's freezing outside".

'''
girdi = int(input('bir sıcaklık değeri giriniz : '))

if girdi < 0:
    print('dışarısı çok soğuk.')

'''

# Soru 22 : If the square of x is less than 100, print "Square of x is less than 100".

'''
girdi = int(input('bir sayı giriniz : '))

if girdi**2 < 100:
    print('girdiğiniz sayının karesi 100 den küçüktür.')

'''

# Soru 23 : If the number is positive, print "The number is positive".

'''
girdi = int(input('bir sayı giriniz : '))

if girdi > 0:
    print('sayı pozitiftir.')
elif girdi == 0:
    print('sayı nötr')

else:
    print('sayı negatiftir.')

'''

# Soru 24 : If the name starts with 'A', print "Name starts with A".

'''
girdi = input('bir isim giriniz : ')

if girdi.startswith('A'):
    print('isim A ile başlıyor.')

'''

# Soru 25 : If the variable is defined, print "Variable is defined".

'''
girdi = (input('değişken ismi giriniz : '))

degisken = 'python'

if girdi == 'python':
    print('değişken tanımlanmış.')

else:
    print('değişken tanımlanmamış.')

'''

# Soru 26 : If the value is divisible by 3, print "Value is divisible by 3".

'''
girdi = int(input('bir sayı giriniz : '))

if girdi % 3 == 0:
    print('girdiğiniz sayı 3 e tam bölünebilir.')

else:
    print('girdiğiniz değer 3 e tam bölünemez.')

'''

# Soru 27 : If the count is greater than 10, print "Count is greater than 10".

'''
girdi = int(input('bir sayı giriniz : '))

if girdi >= 10:
    print('girdiğiniz sayı 10 a eşit yada 10 dan büyük bir sayıdır.')

else:
    print('girdiğiniz sayı 10 dan küçük bir sayıdır.')

'''

# Soru 28 : If the list is empty, print "List is empty".

'''
liste = []

for i in liste:
    print(i)
print('liste boştur.')

'''
# Soru 29 : If the year is a leap year, print "Leap year".

'''
girdi = int(input('bir yıl giriniz : '))

if girdi % 4 == 0:
    print('girdiğiniz yıl artık yıldır.')
else:
    print('girdiğiniz yıl artık yıl değildir.')

'''

# Soru 30 : If the string contains 'hello', print "Hello found".

'''
liste = ['hello', 'dünya', 'world', 'merhaba']

for i in liste:
    if i == 'merhaba':
        print('liste içinde merhaba kelimesi bulundu.')

'''

# Soru 31 : If the price is discounted, print "Discount applied".

'''
girdi = int(input('bir fiyat tutarı yazınız : '))

ürünün_orjinal_fiyatı = 5000

ürünün_indirimli_fiyatı = 4000

if girdi == 5000:
    print('üründe indirim uygulanmamıştır.')
elif girdi == 4000:
    print('üründe indirim uygulanmıştır.')
else:
    print('ürünün böyle bir fiyatı yoktur.')

'''

# Soru 32 : If the hour is between 9 AM and 5 PM, print "Business hours".

'''
girdi = int(input('lüften bir saat giriniz : '))

calisma_saatleri = [9.00,10.00,11.00,12.00,13.00,14.00,15.00,16.00,17.00]

for i in calisma_saatleri:
    if i == girdi:
        print(f'saat {girdi} çalışma saatleri içersindedir.')

'''

 # Soru 33 : If the user input is not 'no', print "User didn't say no".

'''
while True:
    girdi = input('bir kullanıcı adı yazınız : ')

    kullanıcı_adı = ['abc123']

    if girdi != 'hayır':
        print('kullanıcı hayır demedi')

        for i in kullanıcı_adı:
            if girdi == i:
                print('kullanıcı girişi başarılı.')
            else:
                print('kullanıcı adınız hatalı!')
    else:
        print('kullanıcı hayır ifadesini kullandı ve döngü bitti.')
        break

'''

# Soru 34 : If the condition is true, print "Condition is true".

'''
girdi = int(input('bir sayı giriniz : '))

sayı1 = 100

sayı2 = 200

if sayı1 < girdi < sayı2:
   print('koşul doğru')
else:
   print('koşul yanlış')

'''

# Soru 35 : If the day is Thursday, print "Almost there".

'''
while True:
    girdi = input('bir gün adı yazınız : ')

    günler = ['pazartesi', 'salı', 'çarşamba', 'perşembe', 'cuma', 'cumartesi', 'pazar']


    if girdi == günler[3]:
        print('perşembe günündeyiz.')
        break

'''


# Soru 36 : If the result is not zero, print "Result is not zero".

'''
sayı1 = int(input('bir sayı giriniz : '))
sayı2 = int(input('bir sayı giriniz : '))

sayı3 = sayı1 + sayı2

if sayı3 != 0:
    print(f'sonuç sıfır değildir. sonuç {sayı3} dir.')

else:
    print('sonuç sıfırdır.')

'''

# Soru 37 : If the value is negative, print "Value is negative".

'''
sayı1 = int(input('bir sayı giriniz : '))
sayı2 = int(input('bir sayı giriniz : '))

if sayı1 > sayı2:
    result = sayı2 - sayı1
    print(f'bu işlemin sonucu {result} negatif bir sayıdır.')

else:
    print('değer pozitiftir.')

'''

# Soru 38 : If the sum is greater than 100, print "Sum is greater than 100".

'''
liste = [5,10,15,20,25,30]

toplam = 0

for i in liste:
    toplam += i
    if toplam > 100:
        print('toplam 100 den büyüktür.')
    
'''

# Soru 39 : If the number is a prime, print "Number is prime".

'''
while True:
    asal_sayı_kontrol = 0
    sayı = int(input('bir sayı giriniz : '))

    for i in range(2, sayı):
        if sayı % i == 0:
            asal_sayı_kontrol += 1
            
            
    if asal_sayı_kontrol == 0:
        print(f'{sayı} sayısı asaldır.')
        break
    
    else:
        print(f'{sayı} sayısı asal değildir.')

'''
# Soru 40 : If the product is less than 50, print "Product is less than 50".

'''
import time

ürün_sayısı = int(input('ürünün sayısını giriniz : '))

while ürün_sayısı >= 50:
    time.sleep(1)
    print(ürün_sayısı)
    ürün_sayısı -= 1

    if ürün_sayısı == 50:
        
        print('son 1 adet ürün kaldı')
        time.sleep(3)
        continue
    if ürün_sayısı < 50:
        print('ürün sayısı 50 den küçüktür.')

'''

# Soru 41 : If the username is valid, print "Username accepted".

'''
while True:
    kullanıcı_adları = ['abc123', 'bca123', 'cab123']

    username = input('bir kullanıcı adı giriniz : ')

    if username in kullanıcı_adları:
        print(f'girmiş olduğunuz kullanıcı adı {username} geçerlidir.')

    else:
        print(f'girmiş olduğunuz kullanıcı adı {username} geçersizdir.')

'''

# Soru 42 : If the key exists in the dictionary, print "Key found".

'''
sözlük = {'AHMET' : 35, 'MEHMET': 40, 'ALİ' : 50, 'VELİ' : 60}

anahtar_kelime = 'VELİ'

for i in sözlük:
    print(i)
    if i == anahtar_kelime:
        print(f'anahtar kelime {anahtar_kelime} bulundu.')

'''

# Soru 43 : If the string is not empty, print "String is not empty".

'''
liste = ['a', 'b', 'c']

eleman_sayısı = 0

for i in liste:
    print(i)
    eleman_sayısı += 1
print(eleman_sayısı)

if eleman_sayısı == 0:
    print('dizi boş')
else:
    print('dizi boş değil')

'''

# Soru 44 : If the character is a vowel, print "Vowel found".

'''
girdi = input('bir cümle yazınız : ')

sesli_harfler = 'aeıioöuü'

sesli_harf_adedi = 0

for i in girdi:
    if i in sesli_harfler:
       sesli_harf_adedi += 1
print('sesli harf adedi : ', sesli_harf_adedi)

'''
# Soru 45 : If the quantity is zero, print "Out of stock".

'''
girdi = int(input('bir sayı giriniz : '))

if 1 <= girdi:
   print('ürün stokta mevcuttur.')
elif girdi == 0:
   print('ürün stokta mevcut değildir.')

'''

# Soru 46 : If the input is an integer, print "Input is an integer".

'''
girdi = int(input('bir sayı giriniz : '))

tam_sayılar_listesi = [5,6,7,8,9]

if girdi in tam_sayılar_listesi:
    print('girdiğiniz sayı tamsayıdır.')

'''

# Soru 47 : If the condition evaluates to false, print "Condition is false".

'''
while True:
    girdi = int(input('bir rakam giriniz :'))

    sayı = 10

    if girdi > sayı:
        print('koşul doğrudur')
    
    elif girdi == sayı:
        continue

    else:
        print('koşul yanlıştır')
        break
        
'''

# Soru 48 : If the value is greater than 1000, print "Value is huge".

'''
sayı = int(input('bir sayı giriniz : '))

while sayı > 0:
    sayı += 1
    print(sayı)
    
    if sayı > 1000:
        print('sayı 1000 den büyüktür. Değer çok büyük.')
        break

'''

# Soru 49 : If the number is odd, print "Number is odd".

'''
while True:

    sayı = int(input('bir sayı giriniz : '))

    if sayı % 2 == 1:
        print('sayı tektir.')

    elif sayı % 2 == 0:
        print('sayı çifttir.')
        break

'''

# Soru 50 : If the username is not taken, print "Username available".

'''
while True:
    kullanıcı_adları = ['abcd1234', 'efgh1234', 'jklm1234']

    kullanıcıadı = input('bir kullanıcı adı yazınız : ')

    if kullanıcıadı not in kullanıcı_adları:
        print('kullanıcı adı listede mevcut değildir.')

    else:
        print('kullanıcı adı listede mevcuttur.')
        break
        
'''

# Soru 51 : If the character is uppercase, print "Uppercase character".

'''
girdi = input('bir yazı yazınız : ')

büyük_harler_dizisi = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'

büyük_harf_adedi = 0

for i in girdi:
    if i in büyük_harler_dizisi:
        büyük_harf_adedi += 1
    print(f'{büyük_harf_adedi} adet büyük harf vardır.')
print('büyük harf karakteri ile karşılaşıldı.')

'''

# Soru 52 : If the condition is not met, print "Condition not met".

'''
while True:

    girdi = int(input('bir sayı giriniz : '))

    if girdi % 5 != 0:
        print('bu sayı 5 e tam bölünmüyor koşul sağlanmadı.')
        break

    else:
        print('bu sayı 5 e tam bölünmektedir.')

'''
# Soru 53 : If the number is a multiple of 5, print "Number is a multiple of 5".

'''
while True:
    girdi = int(input('bir sayı giriniz : '))

    sayı = 5

    if girdi % sayı == 0:
        print(f'girdiğiniz sayı olan {girdi} beş sayısının katıdır.')
    else:
        print(f'girdiğiniz sayı olan {girdi} beş sayısının katı değildir.')

'''
# Soru 54 : If the word is in the sentence, print "Word found in sentence".

'''
while True:

    cümle = input('bir cümle yazınız : ')

    aranan_kelime = 'hello'

    if aranan_kelime in cümle:
        print(f'aranan kelime olan {aranan_kelime} cümle içersinde mevcuttur.')
        break
    else:
        print(f'aranan kelime olan {aranan_kelime} cümle içersinde mevcut değildir.')

'''

# Soru 55 : If the element is in the set, print "Element found in set".

'''
while True:
    girdi = input('bir meyve ismi yazınız : ')

    küme = set(['armut', 'üzüm', 'karpuz', 'erik'])

    if girdi in küme:
        print('girdiğiniz meyve küme içersinde mevcuttur.')
            
    else:
        print('girdiğiniz meyve küme içersinde mevcut değildir.')
        break
        
'''

# Soru 56 : If the variable is initialized, print "Variable is initialized".

'''
import time

girdi = int(input('bir sayı giriniz : '))

sayı = 0

while girdi > 0:
    print('değişken başlatıldı ve devam ediyor.')
    sayı += 1
    print(sayı)

    if sayı == 50000:
       time.sleep(3)
       continue
    
    if sayı == 100000:
        print('değişken bitiriliyor.')
        time.sleep(3)
        break
        
'''
# Soru 57 : If the item is in the shopping cart, print "Item in shopping cart".

'''
while True:
    ürün_adı = input('bir ürün adı yazınız : ')

    alısveris_sepeti = ['bilgisayar', 'televizyon', 'telefon', 'buzdolabı', 'ütü']

    if ürün_adı in alısveris_sepeti:
        print(f'girmiş olduğunuz ürün olan {ürün_adı} alışveriş sepetinde mevcuttur.')
    else:
        print(f'girmiş olduğunuz ürün olan {ürün_adı} alışveriş sepetinde mevcut değildir.')
        break

'''

# Soru 58 : If the angle is acute, print "Angle is acute".

'''
while True:
    girdi = int(input('bir açı derecesi girin : '))

    if 0 < girdi < 90:
        print('girdiğiniz açı dar açıdır.')

    elif girdi == 90:
        print('girdiğiniz açı dik açıdır.')

    elif 90 < girdi < 180:
        print('girdiğiniz açı geniş açıdır.')
    
    else:
        print('salla gitsin')

'''

# Soru 59 : If the event is canceled, print "Event canceled".

'''
import time

sayma_sayısı = 1
girdi = int(input('bir sayı giriniz : '))

while girdi > 0:
    sayma_sayısı += 5
    print(sayma_sayısı)

    if sayma_sayısı > 500000:
       print('sayma sayısı 500 bini geçti 3 saniye sonra etkinlik iptal edilecek.')
       time.sleep(3)
       break
       
'''

# Soru 60 : If the value is a string, print "Value is a string".

'''
liste = ['merhaba']

for i in liste:
    if type(i) == str:
        print('bu bir string ifadedir.')

liste2 = [123]

for j in liste2:
    if type(j) == int:
        print('bu bir integer ifadedir.')

liste3 = [23.56]

for m in liste3:
    if type(m) == float:
        print('bu bir float ifadedir.')

''' 

# Soru 61 : Kullanıcıdan username, password, kilo, boy bilgisini alınız.
# vücut kitle indeksini hesaplayınız.

'''
x = input('username : ')
y = input('password : ')

if x == 'beast' and y == '123':
    print('login oldunuz.')
    a = float(input('kilonuzu giriniz : '))
    b = float(input('boyunuzu giriniz : '))

    vki = a / b ** 2

    if 0 <= vki <= 18.5:
        print(f"zayıfsınız : {vki}")
    
    elif 18.6 <= vki <= 24.9:
        print(f"normalsiniz : {vki}")

    elif 25 <= vki <= 29.9:
        print(f"kilolusunuz : {vki}")

    elif vki >= 30:
        print(f"obezsiniz {vki}")
    
    else:
        print('doğru değerleri giriniz!!!')

else:
    print('kullanıcı adınızı yada şifrenizi yada her ikisinide yanlış girdiniz. tekrar deneyin!!')

'''

liste = [12, 12, 'True', True, 5, 'ahmet']
print(len(liste))
print(set(liste))

print(len(liste) == len(set(liste)))

        
   





        




    













   





  

    




    



   






        
        














