print('Karar Verme Hesaplama Sayfasina Hosgeldiniz...')

#ALTERNATİFLER
alternatifler = []
alternatifAdet = int(input('kaç adet alternatif eklemek istiyorsunuz: '))
j = 0
while(j<alternatifAdet):
    alternatifName = input((j+1).__str__() + ". alternatif giriniz: ")
    alternatifler.append({
        (j+1).__str__()+'. Alternatif: ': alternatifName,
    })
    j += 1

#DOGAL DURUMLAR
dogalDurumlar = []
dogalDurumAdet = int(input('kaç adet alt durumunuz var: '))
i = 0
while(i<dogalDurumAdet):
    dogalDurumName = input((i+1).__str__() + ". Alt durum giriniz: ")
    dogalDurumlar.append({
        (i+1).__str__()+'. Dogal Durum: ': dogalDurumName,
    })
    i += 1

#DEGER ALMA
degerler = []
degerlerx = []
sayac2 = 0
for alternatif in alternatifler:
    if sayac2 <= len(alternatifler):
        print((sayac2+1).__str__() + ". satır degerlerini giriniz...")
        sayac1=0
        for dogalDurum in dogalDurumlar:
            if sayac1 <= len(dogalDurumlar):
                deger = int(input((sayac1+1).__str__() + ". degeri giriniz: "))
                sayac1 += 1
            degerler.append(deger)
        degerlerx.append(degerler)
        degerler = []
    sayac2 += 1
print(degerlerx)


#EN BÜYÜK
print("EN BÜYÜK DEĞERLER: ")
maxValues = []
for i in degerlerx:
    enBuyukler = [max(i)]
    maxValues.append(enBuyukler)
    print(enBuyukler.__str__())

# EN KUCUK
print("EN KÜÇÜK DEĞERLER: ")
minValues = []
for i in degerlerx:
    enKucukler = [min(i)]
    minValues.append(enKucukler)
    print(enKucukler.__str__())

print(" ")
#İYİMSERLİK KAZANÇ
print("İyimserlik kazanç: " + max(maxValues).__str__())
print(" ")
#İYİMSERLİK MALİYET
print("İyimserlik maliyet: " + min(minValues).__str__())
print(" ")
#KÖTÜMSERLİK KAZANÇ
print("Kötümserlik kazanç: "+max(minValues).__str__())
print(" ")
#KÖTÜMSERLİK MALİYET
print("Kötümserlik maliyet: "+min(maxValues).__str__())
print(" ")
print(" ")


#EŞ OLASILIK
eşOla = 1 / dogalDurumAdet
eşOlDeğerleri = []
değer = 0
toplam = 0
for degerler in degerlerx:
    for i in degerler:
        değer = i * eşOla
        toplam +=değer
        değer=0
    eşOlDeğerleri.append(toplam)
    toplam = 0

#EŞ OLASILIK DEĞERLERİ
print("Eş olasılık değerleri: "+str(eşOlDeğerleri))
print("Eş olasılık kazanç: "+max(eşOlDeğerleri).__str__())
print("Eş olasılık maliyet: "+min(eşOlDeğerleri).__str__())
print(" ")
#ALFA DEGER
alfa = float(input("Lütfen alfa değeri giriniz: "))
if (alfa<=0 or alfa>=1):
    alfa = float(input("Yanlış alfa değeri girdiniz, lütfen alfa değeri giriniz: "))

#HURWİCS
hurwics =[]
for degerler in degerlerx:
    sonuc = max(degerler)*alfa + min(degerler)*(1-alfa)
    hurwics.append(sonuc)

#HURWİCS DEĞERLERİ
print("Hurwics değerleri: "+ hurwics.__str__())
print("Hurwics kazanç: "+max(hurwics).__str__())
print("Hurwics maliyet: "+min(hurwics).__str__())


