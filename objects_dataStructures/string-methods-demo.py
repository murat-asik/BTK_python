website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python programlama Rehberiniz (40 saat)"

# 1- "Hello Word" kaarakter dizisinin baş ve sondaki karakterlerini siliniz.
# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri siliniz.
# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapınız.
# 4- "website" değişkeni içerisinde kaç tane a karakteri vardır? 
# 5- "website" www ile başlayıp .com ile bitiyor mu?
# 6- "website" içinde .com ifadesi var mı?
# 7- "course" içindeki karakterlerin hepsi alfabetik mi?
# 8- "Contents" ifadesini satırda 50 karakter içinde yerleştirip sağ ve soluna * ekleyiniz
# 9- "course" karakte dizisindeki tüm boşluk karakterlerini - ile değiştiriniz
# 10- "Hello World" karakter dizisinin "World" ifadesini "There" ile değiştiriniz
# 11- "course" karakter dizisini boşluk karakterlerinden ayırınız

# 1 
# message = " Hello World "
# message = message.strip()
# print(message)

# 2
# message = "www.sadikturan.com"
# message = message.split("w.com")
# 

# 3
# message = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
# message = message.lower()


# 4
# website = "http://www.sadikturan.com"
# message = website.count("a")
# message = website.count("www,0,10") - 0.indexten 10.index e kadar arama yapıyor.

# 5
# website = "http://www.sadikturan.com"
# message = website.startswith("www")
# message = website.endswith("com")

# 6
# website = "http://www.sadikturan.com"
# message = website.find(".com")
# message = website.index("com") - index bilgisini verir
# message = website.rindex("com") - right
# message = website.lindex("com") - left


# 7
# course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
# message = course.isalpha()
# message = course.isdigit()



# 8
# message = "Contents"
# message = message.center(50,"*")
# message = message.ljust(50,"*") - sola yaslar
# message = message.rjust(50,"*") - sağa yaslar

# 9
# course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
# message = course.replace(" ","-")
# message = course.replace(" ","-","5") - sadece 5 karaktere koyar, sonrasını yine boşluk bırakır


# 10
# message ="Hello World"
# message = message.replace("World","There")
# print(message)


#11
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
message = course.split()
print(message)