
''' 
try:
    sayi1 = int(input('sayı1 = '))
    sayi2 = int(input('sayı2 = '))
    print(sayi1 / sayi2)

except ZeroDivisionError:
    print("sayı sıfıra bölünemez...")

'''

'''
try:
    sayi1 = (input('sayı1 = '))
    sayi2 = (input('sayı2 = '))
    print(sayi1 / sayi2)

except TypeError:
    print('string ifade string ifadeye bölünemez.')

'''

'''
try:
    print('bugün hava çok güzel',se)

except NameError:
    print('isim hatası yapılmış..')

'''

'''
try:

   import numpys

except ModuleNotFoundError:
   print('Modul bulunamadı hatası!!')

'''

'''

try:
    import random
    sayı = random.randint(23, 'a')
    print(sayı)

except TypeError:
    print('type hatası var. lütfen düzeltiniz!!!')

'''

'''
try:
    i = 1
    i.append(2)

except AttributeError:
    print('öznitelik hatası var. bu hatayı düzeltiniz.')

'''

'''
try:
    sayı1 = int(input('bir sayı giriniz : '))
    sayı2 = int(input('bir sayı giriniz : '))
    print(sayı1 / sayı2)

except (ValueError, ZeroDivisionError):
    print('try bölümünde yazan kodlarda ya sıfıra bölünemez hatası yada değer hatası aldık!!!')

'''

'''
try:
    file = open('hello-world123.txt', 'r')
    print(file)

except FileNotFoundError:
    print('böyle bir dosya bulunamadı hatası aldık!!!')

finally:
    print('her durumda finally yazılır!!!!')

'''

'''
try:
    isim = 'ahmet'
    karakter = isim[5]
    print(karakter)

except IndexError:
    print('indekslemede bir hata var.')

finally:
    print('her koşulda çalışır.')

'''

'''
try:
    a = 6
    b = 2
    c = a / b
    print(a)
    print(b)
    print(c)
    
    x = 1000
    d = x
    print(d)

    isim = 'mehmet'
    karakter = isim[5]
    print(karakter)

    dosya = open('hello-world.txt', 'r')
    print(dosya)

except ZeroDivisionError:
    print('sayılar sıfıra bölünemez.')

except NameError:
    print('bu değişken daha önce tanımlanmamış.')

except IndexError:
    print('böyle bir index bulunmuyor.')

except Exception:
    print('bilinmeyen bir hata oluştu!!!')

else:
    print('else bloğu çalışıyor...')

finally:
    print('finally bloğu çalışıyor.')

'''

'''
try:
    a = 6
    b = 2
    c = a / b
    print(a)
    print(b)
    print(c)
    
    x = 1000
    d = x
    print(d)

    isim = 'mehmet'
    karakter = isim[5]
    print(karakter)

    dosya = open('hello-world.txt', 'r')
    print(dosya)

except ZeroDivisionError as z:
    print(z)

except NameError as n:
    print(n)

except IndexError as i:
    print(i)

except Exception as e:
    print(e)

else:
    print('else bloğu çalışıyor...')

finally:
    print('finally bloğu çalışıyor.')

'''

'''
turkce_karakterler = ['ç', 'ş', 'ı', 'ğ', 'ö', 'ü']

isim = input('bir isim giriniz : ')

for i in isim:
    if i in turkce_karakterler:
        raise Exception('türkçe karakterler kullanmayalım..')

print(isim)

'''

'''
print(1)
print(2)

try:
    print(x)

except:
    print('x değişkeni tanımlanmamış..')

print(3)
print(4)

try:
    import numpys

except:
    print('modül isminde hata yakaladık..')

print(5)
print(6)

try:
    sayı1 = 12
    sayı2 = 0
    sayı3 = sayı1 / sayı2
    print(sayı3)

except:
    print('sıfıra bölünemez hatası yakaladık..')

print(7)
print(8)

'''

'''
try:
    num1 = 10
    num2 = int(input('bir sayı girin : '))
    result = num1 / num2
    print(result)
    print(50)
    print(100)

except:
    print('sıfıra bölünemez hatası mevcut..')

'''

'''
try:
    num1 = 5
    num2 = int(input('bir sayı giriniz : '))
    result = num1 / num2
    print(result)

    dosya = open('hello-world.txt')
    
    b = 25
    a = b
    print(a)

except ZeroDivisionError:
    print('sıfıra bölünemez hatası tespit ettik!!')

except ValueError:
    print('string bir ifade tespit ettik.')

except FileNotFoundError:
    print('böyle bir dosya bulunamadı hatası tespit ettik..')

except:
    print('tanımı yapılmamış bir hata tespit ettik...')

else:
    print('hiçbir hata tespit edemedik..')

finally:
    print('her durumda finally komutu çalışır!!')

'''

'''
num1 = 10
num2 = 0

if num2 == 0:
    raise Exception('değer 0 olamaz!!')

print(num1 / num2)
print('hello')

'''

'''
yazı = input('bir şeyler yazınız : ')

if yazı == 'hello':
    raise Exception('lütfen hello kelimesini yazmayınız!!!')

print(yazı)

'''

'''
try:
    islem = input('lütfen değer giriniz : ')

    if islem == '1':
        raise ValueError('int hatası')
    if islem == '2':
        raise NameError('isim hatası')
    if islem == '3':
        raise IndexError('index hatası')
    if islem == '4':
        raise TypeError('tip hatası')

except ValueError:
    print('lütfen int gir')

except NameError:
    print('lütfen ismi düzelt')

except IndexError:
    print('lütfen indeksi düzelt')

except TypeError:
    print('lütfen tipi düzelt')

'''

'''
while True:
    try:
        ders_notu = float(input('lütfen bir ders notu giriniz : '))

        if ders_notu < 0 or ders_notu > 100:
            raise ValueError('geçersiz bir ders notu')

    except ValueError:
        print('lütfen doğru düzgün bir ders notu giriniz!!!')

    else:
        if ders_notu >= 50:
            print('geçtiniz...')
            break
        else:
            print('kaldınız...')
            break

    finally:
        print('dersi geçsenizde dersten kalsanızda bu blok hep çalışır!!!')

'''

'''
def tam_sayiya_cevir():
    girdi = (input('bir ondalık sayı giriniz : '))

    try:
        yuvarla = float(girdi)
        print(f"yuvarlama işleminin sonucu : {round(yuvarla)}")
    
    except:
        print(f"{girdi} girdisi ondalık tipe çevrilemiyor.")
        print(5 *5)

tam_sayiya_cevir()

'''
 

'''
durum = ''

try:
    ders_notu = float(input('bir ders notu giriniz : '))
    
    if ders_notu >= 0 or ders_notu <= 100:
        if ders_notu >= 50:
            print('geçtiniz')
        
        else:
            print('kaldınız')
        
        durum = 'durum başarılı'

except:
    print('string ifade ile ders notu girilemez!!!')
    durum = 'durum başarısız'

finally:
    print(f"tam sayıya çevirme işlemi {durum} olarak tamamlandı!")

'''

'''
while True:
    try:
        sayı1 = int(input('bir sayı giriniz : '))
        sayı2 = int(input('bir sayı giriniz : '))
        sonuc = sayı1 / sayı2
        print(f"sayı1 in sayı2 ye bölümünden kalan sonuç = {sonuc}")
        
    except ZeroDivisionError:
        print('sayı2 değerine sıfır giremezsiniz!!!')
    
    except ValueError:
        print('sayı1 yada sayı2 ye yada her ikisinede string bir ifade giremezsiniz!!')
    
    else:
        print('her hangi bir sorunla karşılaşılmadı else bloğu çalıştı...')
        break
        
    
    finally:
        print('ister bir hatayla karşılaşılsın isterse herhangi bir hata ile karşılaşılmasın finally bloğu her durumda çalışır...')

'''

'''
try:
    sayı = 5
    yazı = '15'
    print(sayı + yazı)

except TypeError:
    print('integer değer ile string ifade toplanamaz!!!')

else:
    print('else bloğu çalıştı..')

finally:
    print('her durumda çalışır..')

'''

'''
try:
    liste = ['ali', 'veli', 'ahmet', 'mehmet', 'cem']

    print(liste[4])

except IndexError:
    print('listede böyle bir indeks bulunamadı')

else:
    print('else bloğu çalıştı.')

finally:
    print('finally bloğu her durumda çalışır.')

'''

'''
try:
    personel = {'ad' : 'cem',
                'soyad' : 'doğan',
                'tc_kimlik_no' : 12312312312}

    print(personel['meslek'])

except KeyError:
    print('böyle bir anahtar kelime bulunamadı...')

else:
    print('else bloğu çalıştı...')

finally:
    print('her durumda çalışır!!!')

'''
'''
try:
    sayı1 = int(input('bir sayı giriniz :'))
    sayı2 = int(input('bir sayı giriniz :'))

    print(sayı1 / sayı2)

except Exception as e:
    print(f"{e}")

'''

'''
try:
    liste = ['a', 'b', 'c']
    print(liste[3])

except Exception as e:
    print(f"{e}")

'''

'''
try:
    karakter1 = 15
    karakter2 = '20'
    print(karakter1 + karakter2)

except Exception as e:
    print(f"{e}")

'''

'''
try:
    personel = {'isim' : 'mehmet', 
                'soyisim' : 'emin', 
                'meslek' : 'yazılımcı'}
    print(personel['yaş'])

except Exception as e:
    print(f"{e}")

'''

'''
try:
    liste = ['a', 'b', 'c', 'd']
    print(liste[0])

    sayı1 = int(input('bir sayı girin : '))
    sayı2 = int(input('bir sayı girin : '))
    print(sayı1 / sayı2)

    karakter1 = int(input('bir sayı girin : '))
    karakter2 = int(input('bir sayı girin : '))
    print(karakter1 + karakter2)

    personel = {'ad' : 'ali', 'soyad' : 'metin', 'meslek' : 'yazılımcı'}
    print(personel['meslek'])

    x = 'merhaba'
    y = x
    print(y)

    dosya = open('hello-world.txt')
    print(dosya)

    

except IndexError as i:
    print(f"{i}")

except ZeroDivisionError as z:
    print(f"{z}")

except ValueError as v:
    print(f"{v}")

except KeyError as k:
    print(f"{k}")

except NameError as n:
    print(f"{n}")

except FileNotFoundError as f:
    print(f"{f}")

except Exception as e:
    print('tanıttığımız hatalar dışında bir hata ile karşılaştık!!!')
    print(f"{e}")

else:
    print('herhangi bir hata ile karşılaşmadık ve else bloğu çalıştı...')

finally:
    print('finally bloğu her durumda çalışır!!!')

'''

'''
sayı1 = int(input('bir sayı giriniz : '))

if sayı1 == 30:
    raise Exception('bu programda 30 sayısını görmek istemiyorum!!!')

sayı2 = int(input('bir sayı giriniz : '))

print(sayı1 / sayı2)

'''

'''
turkce_karakterler = 'şçğüöı'

parola = input('bir parola giriniz : ')

for i in parola:
    if i in turkce_karakterler:
        raise TypeError('parolada türkçe karakter kullanılamaz!!')
    else:
        pass
print('parolanız kabul edildi...')

'''

'''
girdi = input('bir isim giriniz : ')

if len(girdi) == 0:
    raise AssertionError('isim bölümü boş!!')
print(f'hoşgeldin {girdi} ...')

'''

'''

def string_ters_cevir(yazı):
    if (type(yazı) != str):
        raise ValueError('lütfen string bir değer giriniz...')
    else:
        return yazı[::-1]

print(string_ters_cevir(12345))

'''

'''
def topla(sayı1, sayı2):
    if type(sayı1) != int or type(sayı2) != int:
        raise Exception('lütfen integer değer giriniz...')
    
    else:
        return sayı1 + sayı2

print(topla('15', 'ab'))

'''

# Soru 1 : Try-except block to handle division by zero error.

'''
try:
    sayı1 = int(input('bir sayı giriniz : '))
    sayı2 = int(input('bir sayı giriniz : '))

    print(sayı1 / sayı2)

except ZeroDivisionError as z:
    print(f"{z}")
    print('sıfıra bölünemez hatası tespit edildi.')

'''

# Soru 2 : Try-except block to handle type error when converting a string to an integer.

'''
try:
    karakter = int(input('bir karakter giriniz  : '))
    if karakter == str:
        raise ValueError('lütfen bir tamsayı giriniz...')
    else:
        print(karakter)

except ValueError as v:
    print(f"{v}")

'''

# Soru 3 : Try-except block to handle file not found error.

'''
try:
    dosya_adı = open('hello-worldxxx.txt')
    print(dosya_adı)

except FileNotFoundError:
    print('aranan dosya bulunamadı..')

'''

# Soru 4 : Try-except block to handle index error when accessing elements in a list.

'''
try:
    liste = ['a', 'b', '123', 123]
    print(liste[10])

except IndexError as i:
    print(f"{i}")
    print('listede böyle bir index numarası döndürülemiyor!!')

'''

# Soru 5 : Try-except block to handle key error when accessing elements in a dictionary.

'''
try:
    personel = {'isim' : 'mehmet', 
                'yaş' : 50, 'maaş' : 20000, 
                'meslek' : 'öğretmen'}

    print(personel['soyisim'])

except KeyError as k:
    print(f"{k}")
    print('sözlük içinde böyle bir anahtar kelime mevcut değil!!!')

'''

# Soru 6 : Try-except block to handle value error when converting a string to float.

'''
try:
    ondalık_sayı1 = float(input('lütfen bir ondalık sayı giriniz : '))
    ondalık_sayı2 = float(input('lütfen bir ondalık sayı giriniz : '))

    print(ondalık_sayı1 + ondalık_sayı2)

except ValueError:
    print(f"girdiğiniz değerler ondalık sayı olmalıdır...")

'''

# Soru 7 : Try-except block to handle attribute error when accessing an attribute of an object.

'''
try:
    x = 5
    x.insert(10)
    print(x)

except AttributeError as a:
    print(f"{a}")
    print('x değişkeninin böyle bir özniteliği mevcut değildir!!')

'''

# Soru 8 : Try-except block to handle keyboard interrupt error.

'''
while True:
    try:
       sayı = int(input('bir sayı giriniz : '))
       print(sayı)
    
    except ValueError:
        print('lütfen integer bir sayı giriniz...')
    
    except KeyboardInterrupt:
        print('kullanıcı tarafından iptal edildi!!!')
        break
        
'''

# Soru 9 : Try-except block to handle import error when importing a module.
'''
try:
    import abcde

except ModuleNotFoundError as m:
    print(f"{m}")
    print('böyle bir modül ismi yok...')

'''

# Soru 10 : Try-except block to handle name error when accessing an undefined variable.

'''
try:
    a = 10
    b = 20

    d = a + b + c
    print(d)

except NameError as n:
    print(f"{n}")
    print('c adında bir değişken tanımlanmamış!!')

'''

'''
try:
    liste = ['a', 'b', 'c']
    print(liste[1])

    x = 12345
    y = x
    print(y)

    sayı1 = 10
    sayı2 = 0
    print(sayı1 / sayı2)

except (IndexError, NameError, ZeroDivisionError) as e:
    print('try bloğunda en az bir kod hatalı!!!')
    print(f"{e}")

else:
    print('try bloğunda herhangi bir hata tespit edilemedi ve else bloğu çalıştı..')

finally:
    print('finally bloğu her durumda çalışır..')

'''
'''
sayı = int(input('bir sayı giriniz : '))

if sayı < 0:
    raise Exception('girilen sayı negatif olamaz!!!')
print(sayı)

'''

'''
x = '123'

if not type(x) is int:
    raise TypeError('değer sadece tam sayı olabilir!!')
print(x)

'''

'''
try:
    file = open('yazı55.txt')
    file.write('buraya birşeyler yazalım')

except IOError:
    print('dosya bulunamadı veya okunamadı hatası!!')

else:
    print('yazılan içerik başarılı bir şekilde yazıldı...')
    file.close()

'''






# 1: Liste elemanları içerisindeki sayısal değerleri bulunuz.

'''
liste = ['a', 'b', 12, 51.8, 'abc', 90, 68.335]

liste2 = []

for i in liste:
    try:
        i = float(i)
        i = int(i)
    
    except Exception:
        print('bir hata tanımlandı!!!')

    else:
        liste2.append(i)

print(liste2)

'''

# 2: Kullanıcı 'q' değerini girmedikçe girilen her inputun sayı olduğunu doğrulayınız.

'''
sayı_listesi = []

sayac = 0
while True:
    girdi = input('bir karakter giriniz : ')
    try:
        if girdi == 'q':
           break
        girdi = int(girdi)
    
    except Exception as e:
        print('geçersiz değer')
        print(f"{e}")
        break
    
    else:
        sayı_listesi.append(girdi)
        sayac += 1
        if sayac == 5:
            break
print(sayı_listesi)

'''


# 3: Girilen parola içerisinde Türkçe karakter hatası veriniz.

'''
türkce_karakterler = 'çğıöşü'

parolalar = []

sayac = 0

while True:
    
    parola = input('lütfen bir parola giriniz : ')
    
    try:
        
        for i in parola:
            if i in türkce_karakterler:
                raise Exception('parola içersinde türkçe karakterler bulunamaz..')
          
    except Exception:
        print('lütfen parola içinde türkçe karakter bulundurmayınız.')
        break
    
    else:
        print('else bloğu çalıştı.')
         
        parolalar.append(parola)
        sayac += 1
        if sayac == 3:
            break

print(parolalar)

'''

'''
def isim_kontrol(isim):
    türkce_karakterler = 'şİıüÜğĞŞÖöÇç'
    for i in isim:
        if i in türkce_karakterler:
            raise Exception('türkçe karakterler kullanmayınız..')

while True:
    parola = input('lütfen bir parola giriniz : ')
    try:
        isim_kontrol(parola)
    
    except Exception as e:
        print(f"{e}")
    
    else:
        print(f'parolada herhangi bir türkçe karakter tespit edilmedi. parolanız = {parola}')
        break
        
'''

# 4: Girilen parola içerisinde sesli harfler hatası veriniz.

'''
def sesli_harfler_kontrol(kelime):
    sesli_harfler = 'aAeEıIiİoOöÖuUüÜ123'
    for i in kelime:
        if i in sesli_harfler:
            raise Exception('parola içersinde sesli harf olamaz!!!')

while True:
    parola = input('bir parola giriniz : ')
    try:
        sesli_harfler_kontrol(parola)
    
    except Exception as e:
        print(f'parola içinde sesli harf olmasın!!! {e}')
    
    else:
        print(f'yazdığınız parola içersinde herhangi bir sesli harf bulunamamıştır.. parolanız = {parola}')
        break
        
'''

# 5: Girilen parola içerisinde rakam hatası veriniz.

'''   
def rakamlar_kontrol(kelime):
    rakamlarımız = '0123456789'
    for i in kelime:
        if i in rakamlarımız:
            raise Exception('lütfen parola içersinde rakam kullanmayınız!!!')
    
while True:
        
    parola = input('lütfen bir parola giriniz : ')

    try:
        rakamlar_kontrol(parola)
        
    except Exception as e:
        print(f"parola içersinde rakam kullanılamaz..")
        
    else:
        print(f"girmiş olduğunuz parola içersinde herhangi bir rakam bulunamadı.. parolanız = {parola}")
        break
        
'''

# 6 : Liste elemanları içerisindeki integer değerleri bulunuz.

'''
liste = [14, 15, 16, 'a', 'b', 'c', 'd', 'e']

liste_2 = []

for i in liste:

    if i == str:
           raise Exception('listede string ifadeler olamaz..')
         
    try:
        i = int(i)

    except Exception as e:
        print(f'bir hata var!!! {e}')
    
    else:
        liste_2.append(i)
        
print(liste_2)

'''

# 7: Kullanıcı 123 integer değerini girmedikçe girilen her inputun string olduğunu doğrulayınız.

'''
stringler_listesi = []

sayac = 0

while True:
    
    try:
        girdi = int(input('lütfen bir karakter giriniz : '))
        
        if girdi == 123:
            print('int 123 girdiniz...')
            break
        
        girdi = str(girdi)
    
    except Exception as e:
        print(f"geçersiz değer {e}")
        break

    else:
        stringler_listesi.append(girdi)
        sayac += 1
        if sayac == 5:
            break
print(stringler_listesi)

'''

# 8: Faktoriyeli alınacak değerin uygun değer olmaması halinde hata fırlat.

'''
faktöriyel = 1

carpim = 1

while True:

    try:
        girdi = int(input('bir sayı giriniz : '))
        if girdi <= 0:
            raise Exception('girdiğiniz değer 0 yada negatif bir sayı olamaz!!!')
        for i in range(1, girdi+1):
            faktöriyel *= i * carpim
        print(faktöriyel)
        break
    
    except ValueError as v:
        print(f"girdiğiniz değer string bir ifade olamaz!!! {v}")
    
    except Exception as e:
        print(f"girdiğiniz değer sıfır yada negatif değer olmasın!!! {e}")

'''
# Time kütüphanesini ve while döngüsünü kullanarak KeyboardInterrupt hatasını yakalayınız.
'''
import time

sayac = 0
yazı_adedi = 0

while sayac < 20:
    try:
        print('başlıyoruz.....')
        sayac += 1
        time.sleep(1)
    
    except KeyboardInterrupt as k:
        print(f"program çalışırken programı durdurmaya hakkınız yok! {k}")
    
    else:
        print('selam')
        yazı_adedi += 1
        print(f"else bloğundayız toplamda ekrana {yazı_adedi}. kez 'selam' yazdırabildik!!")
    
    finally:
        print('finally bloğundayız bu blok her daim çalışır...')

'''

# Time kütüphanesini ve while döngüsünü kullanarak ZeroDivisionError hatasını yakalayınız.

'''
import time

sayı1 = 50
sayı2 = 10

while True:
    try:
        result = sayı1 / sayı2
        print(f"{sayı1} / {sayı2} = {result}")
        sayı2 -= 1
        time.sleep(3)
    
    except ZeroDivisionError as z:
        print(f"sayı2'nin değeri 0 a eşit oldu ve bir sayı 0 a bölünemez..{z}")
        break

    finally:
        print(f"burası her durumda çalışan finally bloğu...")

'''

# Time kütüphanesini ve while döngüsünü kullanarak FileNotFoundError hatasını yakalayınız.
# FileNotFoundError hatasını yakalayana kadar olan dosyaların adedini yazdırınız.

'''
import time

bulunan_dosya_sayısı = 0

while True:
    try:
        dosya1 = open('deneme1.txt')
        print(dosya1)
        bulunan_dosya_sayısı += 1
        time.sleep(3)
        
        dosya2 = open('deneme2.txt')
        print(dosya2)
        bulunan_dosya_sayısı += 1
        time.sleep(3)
        
        dosya3 = open('deneme3.txt')
        print(dosya3)
        bulunan_dosya_sayısı += 1
        time.sleep(3)
        
        dosya4 = open('yazı.txt')
        print(dosya4)
        bulunan_dosya_sayısı += 1
        time.sleep(3)
        
        dosya5 = open('hello-world.txt')
        print(dosya5)
        bulunan_dosya_sayısı += 1
        time.sleep(3)

        dosya6 = open('abc.txt')
        print(dosya6)
        bulunan_dosya_sayısı += 1
        time.sleep(3)
    
    except FileNotFoundError as f:
        print(f"bu isimde bir dosya bulunamadı!!{f}")
        break
        
print(f"bulunan dosya sayısı = {bulunan_dosya_sayısı}")

'''

# Boş bir liste oluştur. While döngüsü kullanarak kullanıcıdan alınan
# 5 sayıyı listeye ekle. Kullanıcıdan alınan değer int değilse
# ValueError hatasını yakala. Listeye eklenen sayıların toplamını yazdır.

'''
liste = []

toplam = 0

while len(liste) < 5:
    try:
        girdi = int(input('bir sayı giriniz : '))
        
    except ValueError as v:
        print(f"böyle bir değer giremezsiniz!!{v}")
        
    else:
        liste.append(girdi)
        
for i in liste:
    toplam += i
print(toplam)

print(liste)

'''

# Boş bir liste oluşturun. Kullanıcıdan 10 adet değer alın.
# Kullanıcıdan alınan 10 adet değeri boş listeye ekleyin.
# For döngüsü ile liste elemanlarını indeks sırasına göre yazdırın.
# Eğer indeks sayısı listenin eleman sayısını aşıyorsa IndexError hatası yakalayın.

'''
import time

liste = []

while len(liste) < 10:
    karakter = (input('bir değer giriniz : '))
    liste.append(karakter)

try:
    for i in range(11):
      print(liste[i])       
      time.sleep(1)

except IndexError as i:
   print(f"böyle bir indeks numarası bulunmuyor!!! {i}")

print(liste)

'''
'''
liste = []

try:
    karakter = input('bir değer giriniz : ')
    liste.strip(karakter)

except AttributeError as a:
    print(f"liste değişkeni böyle bir özniteliğe sahip değil!! {a}")

'''





   


        




        


       
    
        

    


    











    

        
















    


    

































    







