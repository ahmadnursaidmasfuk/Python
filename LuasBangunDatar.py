# Progam menentukan luas bangun datar

class BangunDatar:
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name

    # fungsi untuk mencari luas
    def luas(self, order):
        # mencari luas persegi panjang
        if order == 0 :
            panjang=float(input("masukkan nilai panjang bangun: "))
            lebar=float(input("masukkan nilai lebar bangun: "))
            luas = panjang*lebar
        # mencari luas persegi
        if order == 1 :
            sisi=float(input("masukkan nilai sisi bangun: "))
            luas = sisi*sisi
        # mencari luas segitiga
        if order == 2 :
            alas=float(input("masukkan nilai alas bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            luas = 1/2*alas*tinggi
        # mencari luas trapesium
        if order == 3 :
            atas=float(input("masukkan nilai sisi atas bangun: "))
            bawah=float(input("masukkan nilai sisi bawah bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            luas = 1/2*(atas+bawah)*tinggi
        # mencari luas jajar genjang
        if order == 4 :
            alas=float(input("masukkan nilai sisi alas bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            luas = alas*tinggi
        # mencari luas layang - layang
        if order == 5 :
            diagonal1=float(input("masukkan nilai diagonal 1 bangun: "))
            diagonal2=float(input("masukkan nilai diagonal 2 bangun: "))
            luas = 1/2*diagonal1*diagonal2
        # mencari luas belah ketupat
        if order == 6 :
            diagonal3=float(input("masukkan nilai diagonal bangun: "))
            luas = 1/2*diagonal3*diagonal3
        # mencari luas lingkarang
        if order == 7 :
            jari_jari=float(input("masukkan nilai jari - jari bangun: "))
            luas = 3.14*jari_jari*jari_jari

        return luas
       

bangun_item1 = BangunDatar('Persegi')
bangun_item2 = BangunDatar('Persegi Panjang')
bangun_item3 = BangunDatar('Segitiga')
bangun_item4 = BangunDatar('Trapesium')
bangun_item5 = BangunDatar('Jajar Genjang')
bangun_item6 = BangunDatar('Layang - layang')
bangun_item7 = BangunDatar('Belah Ketupat')
bangun_item8 = BangunDatar('Lingkaran')


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

result = selected_bangun.luas(order)

print('Luas bangun datar adalah: '+str(result))
