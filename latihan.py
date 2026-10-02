nim = input("Masukkan NIM: ")

for angka in nim:
    angka = int(angka)

    if angka % 2 == 0:
        print(angka, "adalah bilangan genap")
    else:
        print(angka, "adalah bilangan ganjil")

Kode = 7890
PIN = 4567
n = 1
while n <= 5:
    input_Kode = int(input("Masukkan Kode Anda: "))
    input_PIN = int(input("Masukkan PIN Anda: "))
    if input_Kode == Kode and input_PIN == PIN:
        print("Akses diterima.")
    else:#
        print("Akses ditolak. Kode atau PIN salah silahkan coba lagi.")
    n = n + 1
print("Percobaan Anda sudah habis silahkan hubungi admin untuk mendapatkan akses kembali.")


namaTamu = input("Masukkan Nama Anda: ")
alamatTamu = input("Masukkan Alamat Anda: ")

member = input("Apakah Anda member? (Y/N): ").upper()

if member == "Y" or member == "N":

    if member == "Y":
        print(f"Selamat datang {namaTamu} dari {alamatTamu}, "
              "Anda mendapatkan diskon 20%")#
    else:
        print(f"Selamat datang {namaTamu} dari {alamatTamu}, "
              "Anda tidak mendapatkan diskon")

    jenisKamar = input(
        "Masukkan jenis kamar (Suite/Superior/Deluxe): "
    ).lower()

    if jenisKamar == "suite":
       hargaKamar = 1000000
    elif jenisKamar == "superior":
        hargaKamar = 600000
    elif jenisKamar == "deluxe":
        hargaKamar = 400000
    else:
        print("Jenis kamar tidak valid")
        hargaKamar = 0#\

    if hargaKamar > 0:
        lamaMenginap = int(
            input("Masukkan lama menginap (dalam hari): ")
        )

        totalHarga = hargaKamar * lamaMenginap

        if member == "Y":
            hargaDiskon = totalHarga * 0.2
            hargaAkhir = totalHarga - hargaDiskon
        else:
            hargaAkhir = totalHarga

        print(f"Harga kamar per malam: Rp{hargaKamar:,.0f}")
        print(f"Lama menginap: {lamaMenginap} hari")
        print(f"Total harga yang harus dibayar: Rp{hargaAkhir:,.0f}")

else:
    print("Pilihan member tidak valid. Masukkan Y atau N.")

n = 10
for i in range(1, n + 1):
    for j in range(1, i +1):
        print(i * j, end=" ")
    print()