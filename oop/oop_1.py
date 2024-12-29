# Class adalah blueprint atau cetakan untuk membuat object
class Mobil:
    def __init__(self, merek, model, warna):
        self.merek = merek
        self.model = model
        self.warna = warna
# Memanggil instance dari Class Mobil
instance_mobil = Mobil("toyota", "manual", "putih")
print(f"Merek mobil: {instance_mobil.merek}")
print(f"Model : {instance_mobil.model}")
print(f"Warna: {instance_mobil.warna}")