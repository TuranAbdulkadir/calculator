def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y == 0:
        return "Hata: Sıfıra bölünemez!"
    return x / y

print("Basit Hesap Makinesi")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminiz (1/2/3/4): ")

sayi1 = float(input("Birinci sayı: "))
sayi2 = float(input("İkinci sayı: "))

if secim == '1':
    print("Sonuç:", topla(sayi1, sayi2))
elif secim == '2':
    print("Sonuç:", cikar(sayi1, sayi2))
elif secim == '3':
    print("Sonuç:", carp(sayi1, sayi2))
elif secim == '4':
    print("Sonuç:", bol(sayi1, sayi2))
else:
    print("Geçersiz seçim!")