list=["a", "b", "c", "d", "e"]

print("Tampilkan Element Ke 3 :", list[2])
print("Ambil Element Ke 2 Sampai 4 :", list[1:4])
print("Ambil Element Terakhir :", list[5-1])

# Merubah Nilai Ke 4 Dengan Nilai lain
list[3] = "f"
print("Merubah Nilai Ke 4 Dengan Nilai Lain", list)

# Merubah Element Ke 4 Sampai Dengan Element Terakhir
list[3:] = "f", "g"
print("Merubah Element Ke 4 Sampai Dengan Element Terakhir", list)

# Tampilan Elemen List
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Ambil 2 Bilangan List A Ke List B
b.append(a[1:3])
print("2 Bilangan List A Dijadikan List B :", b)

# Tambah List B dengan 3 Nilai
print("Tambah List B Dengan 3 Nilai :", b+[11,12,13])

# Gabungan Nilai B Dan A
c = b+a
print("Gabungan List B Dan A :", c)

