# Print String menggunakan f-string (cara baru)
nama_depan = "Ronald"
nama_belakang = "Suparmin"
print(f"Hallo, {nama_depan} {nama_belakang}")

# Print menggunakan cara lama %s -- string, %d -->angka (cara baru f("string {variable}"))
nama = "Ronald Suparmin"
usia = 5
print("Nama saya %s usia %s" % (nama, usia))
print(f"Nama saya {nama} usia {usia}")

# exercise
harga_ayam = float(input("Harga Ayam ="))
harga_bumbu = float(input("Harga bumbu ="))
harga_beras = float(input("Harga beras ="))
total_belanja = harga_ayam + harga_bumbu + harga_beras

print(f"total belanja = {total_belanja}")