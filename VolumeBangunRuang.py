# Progam menentukan volume bangun ruang

# Progam mencari volume bangun ruang menggunakan OOP (Object Oriented Programming) dengan menggunakan bahasa pemrograman python. Volume bangun ruang yang dapat dicari adalah :
# 1. Kubus
# 2. Balok
# 3. Prisma
# 4. Limas segitiga
# 5. Limas segiempat
# 6. Tabung
# 7. Kerucut
# 8. Bola

class BangunRuang:
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name

    # fungsi untuk mencari volume
    def volume(self, order):
        # mencari volume kubus
        if order == 0 :
            sisi=float(input("masukkan nilai sisi bangun: "))
            volume = sisi*sisi*sisi
        # mencari volume balok
        elif order == 1 :
            panjang=float(input("masukkan nilai panjang bangun: "))
            lebar=float(input("masukkan nilai lebar bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = panjang*lebar*tinggi
        # mencari volume prisma
        elif order == 2 :
            alas_segitiga=float(input("masukkan nilai alas segitiga alas bangun: "))
            tinggi_segitiga=float(input("masukkan nilai tinggi segitiga alas bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = alas_segitiga*tinggi_segitiga*tinggi/2
        # mencari volume limas segitiga
        elif order == 3 :
            alas_segitiga=float(input("masukkan nilai alas segitiga alas bangun: "))
            tinggi_segitiga=float(input("masukkan nilai tinggi segitiga alas bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = (alas_segitiga*tinggi_segitiga/2)*tinggi/3
        # mencari volume jajar segiempat
        elif order == 4 :
            panjang_alas=float(input("masukkan nilai panjang alas bangun: "))
            lebar_alas=float(input("masukkan nilai lebar alas bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = (panjang_alas*lebar_alas)*tinggi/3
        # mencari volume tabung
        elif order == 5 :
            jari_jari=float(input("masukkan nilai jari -jari bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = (3.14*jari_jari*jari_jari)*tinggi
        # mencari volume kerucut
        elif order == 6 :
            jari_jari=float(input("masukkan nilai jari -jari bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = (3.14*jari_jari*jari_jari)*tinggi/3
        # mencari volume bola
        elif order == 7 :
            jari_jari=float(input("masukkan nilai jari - jari bangun: "))
            volume = 3.14*jari_jari*jari_jari*4/3

        return volume
       

bangun_item1 = BangunRuang('Kubus')
bangun_item2 = BangunRuang('Balok')
bangun_item3 = BangunRuang('Prisma')
bangun_item4 = BangunRuang('Limas Segitiga')
bangun_item5 = BangunRuang('Limas Segiempat')
bangun_item6 = BangunRuang('Tabung')
bangun_item7 = BangunRuang('Kerucut')
bangun_item8 = BangunRuang('Bola')


bangun_items = [bangun_item1, bangun_item2, bangun_item3, bangun_item4, bangun_item5, bangun_item6, bangun_item7, bangun_item8]

index = 0

for bangun_item in bangun_items:
    print(str(index) + '. ' + bangun_item.info())
    index += 1

print('--------------------')

order = int(input('Masukkan nomor bangun yang dipilih: '))
selected_bangun = bangun_items[order]
print('bangun yang di pilih adalah: ', selected_bangun.name)

print('--------------------')

result = selected_bangun.volume(order)

print('volume bangun datar ',selected_bangun.name,' adalah: ',str(result))
