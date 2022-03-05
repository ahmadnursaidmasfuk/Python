class Suhu :
    def __init__(self,name):
        self.name=name
   
    def keterangan(self):
        return self.name
   
    def konversi(self, order1, order2):
        # konversi suhu celsius ke reamur
        if order1 == 0 and order2 == 1:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=4/5*suhu_awal
        
        # konversi suhu celsius ke fahrenheit
        elif order1 == 0 and order2 == 2:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=9/5*suhu_awal+32

        # konversi suhu celsius ke kelvin
        elif order1 == 0 and order2 == 3:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=suhu_awal+273

        # konversi suhu reamur ke celsius
        elif order1 == 1 and order2 == 0:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=5/4*suhu_awal
        
        # konversi suhu reamur ke fahrenheit
        elif order1 == 1 and order2 == 2:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=9/4*suhu_awal+32

        # konversi suhu reamur ke kelvin
        elif order1 == 1 and order2 == 3:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=9/5*suhu_awal+273

        # konversi suhu fahrenheit ke celsius
        elif order1 == 2 and order2 == 0:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=(suhu_awal-32)*5/9
        
        # konversi suhu fahrenheit ke reamur
        elif order1 == 2 and order2 == 1:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=(suhu_awal-32)*4/9

        # konversi suhu fahrenheit ke kelvin
        elif order1 == 2 and order2 == 3:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=(suhu_awal-32+273)*5/9
        
        # konversi suhu kelvin ke celsius
        elif order1 == 3 and order2 == 0:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=suhu_awal-273
        
        # konversi suhu kelvin ke reamur
        elif order1 == 3 and order2 == 1:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=(suhu_awal-273)*4/5

        # konversi suhu kelvin ke fahrenheit
        elif order1 == 3 and order2 == 2:
            suhu_awal=float(input("Masukkan nilai suhu: "))
            suhu_akhir=(suhu_awal-273+32)*9/5

        return suhu_akhir


suhu_item1=Suhu("Celcius")
suhu_item2=Suhu("Reamur")
suhu_item3=Suhu("Fahrenheit")
suhu_item4=Suhu("Kelvin")

suhu_items=[suhu_item1,suhu_item2,suhu_item3,suhu_item4]

index=0
for suhu_item in suhu_items :
    print(index, " satuan suhu: ", suhu_item.keterangan())
    index+=1
print("-------------------")

order1=int(input("silahkan masukkan nomer satuan yang akan dikonversi: "))
select_suhu1=suhu_items[order1]
order2=int(input("silahkan masukkan nomer satuan tujuan dikonversi: "))
select_suhu2=suhu_items[order2]
print("satuan tujuan dikonversi adalah: ", select_suhu1.name)
print("satuan yang akan dikonversi adalah: ", select_suhu2.name)

print("-------------------")


hasil=select_suhu1.konversi(order1,order2)
print("Hasil konversi suhu dari ",select_suhu1.name, " menjadi ", select_suhu2.name, " adalah: ",hasil)
