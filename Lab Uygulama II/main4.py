

yas = int(input("Lütfen yaşinizi girin: "))

if  yas < 2:
    print("Bu kişi bebektir.")
elif 2 <= yas <= 4:
    print("Bu kişi yeni yürümeye başlayan çocuktur.")
elif 4 <= yas <= 13:
    print("Bu kişi çocuktur.")
elif 13 <= yas <= 20:
    print("Bu kişi ergendir.")
elif 20 <= yas <= 65:
    print("Bu kişi yetişkindir.")
else:
    print("Bu kişi yaşlidir.")
