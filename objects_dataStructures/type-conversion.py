x = input('1. sayı: ')
y = input('2. sayı: ')

print(type(x))
print(type(y))

toplam = int(x) + int(y)

print(toplam)

'''
Burada x ve y değerlerini kullanıcan input fonksiyonu ile aldığımızda aldığımız verinin tipini string olarak almaktayız.
Bu değerlerin tipini string olarak aldığımızın kontrolünü print(type(x)) ve print(type(y)) satırlarındaki kodla konntrol edelim.
Program çalıştığında bu değerlerin tipini <class 'str'> <class 'str'> olarak görürüz.
7. satırda yaptığımız değişken değiştirme işlemini yapmasaydık toplam değeri terminal ekranında verdiğimiz satıların string olarak 
işleme alınması sonucu (örneğin 1. sayı 10, 2.sayı 20 olsun) 1020 olarak görürüz.
Veri tiplerini değiştirdiğimiz takdirde 1. ve 2. sayı tipi int olarak işleme alınarak işlem sonucumuzun 30 olduğunu görürüz.
'''

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

#Type Conversion

#int to float

# x = float (x)
# print(x)
# print(type(x))

# y = int(y)
# print(y)
# print(type(y))

# result = x + y
# print(result)
# print(type(result))

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

#isOnline = int(isOnline)
#print(isOnline)
#print(type(isOnline))