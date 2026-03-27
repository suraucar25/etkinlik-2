'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

ort = float(input("Öğrenci Ortalamasını Giriniz:"))
zayif = int(input("Öğrencinin Zayıf Ders Sayısını Giriniz:"))

if zayif == 0:
    if ort >= 85:
        print("Durum: Takdir Belgesi Takdim Edilir.")
    elif ort >= 70:
        print("Durum: Teşekkür Belgesi Takdim Edilir.")
    else:
        print("Durum: Sınıfı geçtiniz.")
else:
    if ort >= 50:
        print("Durum: Sınıfı geçtiniz.")
    elif ort >= 25:
        print("Durum: Ortalama Yükseltme ve Sorumluluk Sınavına giriniz.")
    else:
        print("Durum: Sınıfı tekrar ediniz.")