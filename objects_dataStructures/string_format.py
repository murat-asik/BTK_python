name = 'Murat'
surname = 'Aşık'
age = '25'

# print('My name is {}' .format(name))
# {} ile belirlenen yere tanımlanan değişkenlerden name değişkeni gelecektir.
# print("My name is {} {}".format(name,surname))
# İkinci bir değişken eklemek istenirse tekrardan aynı işlem yapılır.
# print("My name is {0} {1}".format(name,surname))
# Değişkenlerin indeksleri ile de bu işlem yapılabilir.
# print("My name is {1} {0}".format(name,surname))
# print("My name is {s} {n}".format(n=name,s=surname))
# name ve surname değişkenlerini bir değişkene atayarak da işlem gerçekleştirilir.
# print("My name is {n} {s}".format(n=name, s=surname) + " and I am {a}".format(a=age)+ "years old")
# print("My name is {n} {s} and I'm {a} years old".format(n=name, s=surname,a=age) )

result = 864 / 89
print("the result is {r:1.4}" .format(r=result))
# Yapılan işlemde sonucunda kaç basamak görmek istediğimizi bu şekilde belirtiriz.
print("My name is {n} {s}".format(n=name, s=surname) + " and I am {a}".format(a=age)+ "years old")