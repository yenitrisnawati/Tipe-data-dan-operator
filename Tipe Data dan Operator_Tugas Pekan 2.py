#Mengubah tipe data
import math


a=2025
print("Tipe data", a, "adalah", type(a))
b=95.5
print("Tipe data", b, "adalah", type(b))
c="Pemrograman Python"
print("Tipe data", c, "adalah", type(c))
d=9>5
print("Tipe data", d, "adalah", type(d))

#Tampilan data
print("Halo",end=" ")
print("Bagaimana", end=" ")
print("Kabarmu?")
print(" ")

a="Selamat Datang"
print(a,"\n")
b="Selamat Belajar"
print(b,"\n")
c="Selamat Istirahat"
print(c,"\n")

print("NO\tMahasiswa\tNIM")
print("1\tYeni Trisnawati\t108102530001")

#Operator aritmatika
a=21
b=5
hasil = a % b
print("Nilai a=", a)
print("Nilai b=", b)
print("Sisa bagi dari a % b =", hasil)

#Operator pembanding
x = 15
y = 7
hasil = x > y
print("Nilai x =", x)
print("Nilai y =", y)
print("Apakah x lebih besar dari y?", hasil)

#Operator penugasan
total_uang = 400000
print("Total uang sebelum dibagi =", total_uang)
total_uang /=8
print("Setelah dibagi untuk 8 orang, tiap orang mendapat =", total_uang)

#Ketetapan matematika
print("===== KONSTANTA MATEMATIKA =====")
print("Nilai konstanta π (pi):", math.pi)
print("Nilai konstanta e:", math.e)
print("Nilai konstanta τ (tau):", math.tau)

diameter = 10
jari_jari = diameter / 2

keliling = math.tau * jari_jari  # tau = 2π
luas = math.pi * jari_jari**2

print("\n===== HASIL PERHITUNGAN =====")
print("Diameter lingkaran:", diameter)
print("Keliling lingkaran:", keliling)
print("Luas lingkaran:",luas)

#Input variabel
a = input ('Masukkan Panjang: ')
a = int(a)
b = input ('Masukkan lebar: ')
b = int(b)
c = a*b
print(c)