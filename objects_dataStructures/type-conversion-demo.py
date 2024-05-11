'''
Daire alanı ve çevresini hesaplayan bir uygulama yazalım.
Dairenin alan formülü: πr²
Dairenin çevre formülü: 2πr
'''

pi = 3.14
r = float(input('yarıçap: '))
#Yarıçap değerine str gibi bir veri tipi girildiğinde otomatik olarak float değerine çevirmek için yukarıdaki kod satırı yazılmıştır
#Burada veri tipi değiştime uygulanmıştır.
alan = pi * (r**2)
cevre = 2 * pi * r


print('Dairenin alanı: ', alan)
print('Dairenin çevresi:', cevre)
