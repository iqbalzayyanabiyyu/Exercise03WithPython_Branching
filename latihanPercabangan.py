# LATIHAN PERCABANGAN (Python Conditions and If statements)
# M. IQBAL ZAYYAN ABIYYU_12210720_kls.12.1A.39
# Selasa, 5 Oktober 2021 _ Pertemuan04
# Tugas 1
print("PROGRAM HITUNG GAJI KARYAWAN PT.DINGIN DAMAI")
# Gaji Perbulan
gaji = 300000
# Nama
nama = input("Nama Karyawan : ")
# Golongan
golJabatan = int(input("Golongan Jabatan 1/2/3 : "))
# Pendidikan
pendidikan = input("Pendidikan : ")
# Jumlah Jam Kerja
jamLembur = int(input("Jumlah jam kerja : "))

# Layar Keluar
print("--------------------------")
print("Karyawan yang bernama : ", nama)
print("Honor yang diterima")


def myFun():
    def hitungHonorLembur():
        honorLembur = jamLembur * 3500
        print("Honor Lembur : Rp", honorLembur)
        print("Total Gaji : Rp", gaji + (tunjangan + tPendidikan) + honorLembur)

    if pendidikan == "SMA":
        tPendidikan = (2.5/100) * gaji
        print("Tunjangan Pendidikan : Rp", tPendidikan)
        if jamLembur > 8:
            hitungHonorLembur()
    elif pendidikan == "D1":
        tPendidikan = (5/100) * gaji
        print("Tunjangan Pendidikan : Rp", tPendidikan)
        if jamLembur > 8:
            hitungHonorLembur()
    elif pendidikan == "D3":
        tPendidikan = (20/100) * gaji
        print("Tunjangan Pendidikan : Rp", tPendidikan)
        if jamLembur > 8:
            hitungHonorLembur()
    else:
        tPendidikan = (30/100) * gaji
        print("Tunjangan Pendidikan : Rp", tPendidikan)
        if jamLembur > 8:
            hitungHonorLembur()


if golJabatan == 1:
    tunjangan = (5/100) * gaji
    print("Tunjangan Jabatan : Rp", tunjangan)
    myFun()
elif golJabatan == 2:
    tunjangan = (10/100) * gaji
    print("Tunjangan Jabatan : Rp", tunjangan)
    myFun()
else:
    tunjangan = (15/100) * gaji
    print("Tunjangan Jabatan : Rp", tunjangan)
    myFun()
