# Progam menentukan keliling bangun datar
class BangunDatar:
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name

    # fungsi untuk mencari keliling
    def keliling(self, order):
        # mencari keliling persegi panjang
        if order == 0 :
            panjang=float(input("masukkan nilai panjang bangun: "))
            lebar=float(input("masukkan nilai lebar bangun: "))
            keliling = (panjang+lebar)*2
        # mencari keliling persegi
        elif order == 1 :
            sisi=float(input("masukkan nilai sisi bangun: "))
            keliling = sisi*4
        # mencari keliling segitiga
        elif order == 2 :
            a=float(input("masukkan nilai sisi pertama bangun: "))
            b=float(input("masukkan nilai sisi kedua bangun: "))
            c=float(input("masukkan nilai sisi ketiga bangun: "))
            keliling = a + b + c
        # mencari keliling trapesium
        elif order == 3 :
            sisi_sejajar_atas=float(input("masukkan nilai sisi sejajar atas bangun: "))
            sisi_sejajar_bawah=float(input("masukkan nilai sisi sejajar bawah bangun: "))
            sisi_kiri=float(input("masukkan nilai sisi kiri bangun: "))
            sisi_kanan=float(input("masukkan nilai sisi kanan bangun: "))
            keliling = sisi_sejajar_atas + sisi_sejajar_bawah + sisi_kiri + sisi_kanan 
        # mencari keliling jajar genjang
        elif order == 4 :
            sejajar=float(input("masukkan nilai sisi sejajar bangun: "))
            miring=float(input("masukkan nilai sisi miring bangun: "))
            keliling = 2*(sejajar+miring)
        # mencari keliling layang - layang
        elif order == 5 :
            miring_atas=float(input("masukkan nilai sisi miring atas bangun: "))
            miring_bawah=float(input("masukkan nilai sisi miring bawah bangun: "))
            keliling = 2*(miring_bawah+miring_atas)
        # mencari keliling belah ketupat
        elif order == 6 :
            miring=float(input("masukkan nilai sisi miring bangun: "))
            keliling = 4*miring
        # mencari keliling lingkarang
        elif order == 7 :
            jari_jari=float(input("masukkan nilai jari - jari bangun: "))
            keliling = 3.14*2*jari_jari

        return keliling
       

bangun_item1 = BangunDatar('Persegi Panjang')
bangun_item2 = BangunDatar('Persegi')
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

result = selected_bangun.keliling(order)

print('keliling bangun datar ',selected_bangun.name,' adalah: ',str(result))
