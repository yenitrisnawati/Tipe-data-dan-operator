import math
print("=== PROGRAM MENGHITUNG TOTAL BELANJA ===")

#input
nama= input("Masukkan nama anda: ")
barang= input("Masukkan nama barang: ")
harga_input= input("Masukkan harga barang: ")
jumlah_input= input("Masukkan jumlah barang: ")

#Mengubah tipe data
harga= int(harga_input)
jumlah= int(jumlah_input)

#Operator matematika
total= harga * jumlah

#Operator pembanding
if total >= 50000:
    diskon= total * 10 // 100
else:
    diskon= total * 5 // 100

#Operator penugasan
total -= diskon

#Ketetapan matematika
bonus_poin= int((math.pi + math.e) * 10)

#Tampilan data
print("\n=====STRUK PEMBAYARAN=====")
print("Nama Pelanggan\t:" + nama)
print("Nama Barang\t:" + barang)
print("Jumlah Barang\t:" + str(jumlah))
print("Harga Satuan\t:Rp" + str(harga))
print("Diskon\t\t:Rp" + str(diskon))
print("Total Bayar\t:Rp" + str(total))
print("Bonus Poin\t:" + str(bonus_poin))

print("\nTerima kasih telah berbelanja di toko kami!")