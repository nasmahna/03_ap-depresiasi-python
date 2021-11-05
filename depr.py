```
print("="*40)
print("    Aplikasi Penghitung Depresiasi")
print("\tStraight Line Method")
print("="*40)


harga           = float(input("\nHarga Perolehan    = "))
residu          = float(input("Nilai Residu       = "))
umur            = int(input("Umur/ Masa Manfaat = "))
tahun_awal      = int(input("Tahun Awal         = "))
tahun_akhir     = int(input("Tahun Akhir        = "))


def depresiasi(harga, umur, tahun_awal, tahun_akhir, residu):
    if (harga != None and umur != None and tahun_awal != None and tahun_akhir != None and residu != None):
        if (tahun_awal < tahun_akhir):
            print("\n")
            print("="*60)
            print("Tahun ke- ".ljust(15), "Harga Awal".ljust(15), " Akumulasi".ljust(15), "Nilai")
            print("-"*60)
            r = (harga - residu) / umur
            for umur in range (tahun_awal, (tahun_akhir+1), 1):
                akm = umur * r
                nilai_sisa = harga - akm
                print(umur," ".ljust(14), harga," ".ljust(5), akm," ".ljust(5), nilai_sisa)
            print("="*60)
        else:
            print("False")
    else:
        print("STOP!")

depresiasi(harga, umur, tahun_awal, tahun_akhir, residu)
```

