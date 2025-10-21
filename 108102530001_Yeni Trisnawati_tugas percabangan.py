# soal#1 Tamasya

N = int(input("Masukkan Jumlah Mahasiswa"))

hasil = (N // 7) + 1 
bangku_kosong = N & 7

print("Total mobil yang dibutuhkan = ", hasil)
print(N//7, "mobil penuh dan", "1 mobil berisi ", bangku_kosong)

# soal#2 Diskon
total=int(input("masukkan total belanja="))
asesmen=(input("Apakah sedang asesmen(true/false)="))
total_diskon = 0.65 * total
if asesmen.lower ()== "true":
    print ("total belanja anda adalah",total_diskon)

else:
    print("total belanja anda adalah ", total)

# soal#3 Konsonan
huruf = input("Masukkan satu huruf= ")

if not ('a' <= huruf.lower() <= 'z'):
    print()
elif huruf.lower() in ['a', 'i', 'u', 'e', 'o']:
    print("Bukan huruf konsonan")
else:
   print("huruf Konsonan")

# soal#4 Tiga&lima
bilangan_bulat = int(input("masukkan angka"))
if bilangan_bulat % 3 == 0 and bilangan_bulat % 5 == 0:
    print("kelipatan 3 dan kelapatan 5")
elif bilangan_bulat % 3 == 0:
    print("kelipatan 3")
elif bilangan_bulat & 5 == 0:
    print("kelipatan 5")
else:
    print("bukan kelipatan 3 atau 5")

# soal#5 Liga Bola
a = int(input("masukkan gol pertama: "))
b = int(input("masukkan gol kedua: "))
c = int(input("masukkan gol ketiga: "))
d = int(input("masukkan gol keempat: "))

print("a=", a, "b=", b, "c=", c, "d=", d)

total = [a,b,c,d]
terbanyak = max (total)
tersedikit = min (total)
print("terbanyak", terbanyak, "tersedikit", tersedikit)

