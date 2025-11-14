#Hesap makinesi
ilkSayı =int(input("Birinci sayısı giriniz ?"))
ikinciSayıyı = int(input("İkinci sayısı giriniz ?"))

işlem = input("""Hangi işlemi yapamk istiyorsunuz ?
Toplama : +  , Çıkarma : - , Çarpma : *  , Bölme : / """)

if işlem == "+":
    print("Sonuç "+ str(ilkSayı+ikinciSayıyı))
elif işlem == "-":
    print("Sonuç "+ str(ilkSayı-ikinciSayıyı))
elif işlem == "*":
    print("işlem "+int(ilkSayı*ikinciSayıyı))
elif işlem == "/":
    print("Sonuç "+int(ilkSayı/ikinciSayıyı))