barang = int(input('Masukkan Jumlah Barang : '))
total = 0
for i in range(barang):
    harga = int(input(f'Masukkan harga barang {i + 1} : '))
    total += harga
print(15*'=','TOTAL',15*'=')
print('Total Belanjaan : Rp.',total)
print(37*'=')