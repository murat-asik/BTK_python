message = "Hello there. My name is Murat Aşık"

# message = message.upper() - Karakterlerin hepsi büyük harf olarak yazılır
# message = message.lower() - Karakterlerin hepsi küçük harf olarak yazılır
# message = message.capitalize() - Sadece ilk harf büyütülür
# message = message.title() - Her kelimenin ilk harfini büyütür

# message = message.strip() - Özellikle parolalar için kullanılır. Baştaki boşluk yok edilir.
# message = message.split() - Cümle, boşluklarından tek tek bölünür. print(message[]) index ifadesi ile numarasıyla aranabilir.
# message = message.split(".") - Noktalardan itibaren böler.

# message = message.split() -cümle ayrılır, joinle her kelime arasına yıldız koyulur.
# message = "---".join(message)

# index = message.find("Murat") - ilk başladığı index numarasını verir.

# isFound = message.startswith("H") - başlayan harfi
# isFound = message.endswith("o") - biten harf

# message = message.replace("Murat","Aşık") - değiştirme
# message = message.replace("ş","s").replace("ı","i")

# message = message.center(100,"*") -mesajı ortalayıp, 100 karakterlik bir container oluşturulur. *ların ortasına ortalanır.

print(message)