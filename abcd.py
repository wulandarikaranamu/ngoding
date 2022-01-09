pekerjaan = input("pekerjaan anda adalah :")
jumlah_anak = int(input("jumlah anak anda adalah :"))
gaji = int(input("jumlah perbulan anda adalah Rp :"))

if gaji >= 3000000 and gaji < 7000000 :
    pajak = 5/100
    if gaji == "PNS":
        pajak = pajak + 2/100
elif gaji >= 7000000 :
    pajak = 10/100
    if gaji == "PNS":
        pajak = pajak + 2/100
else:
    pajak = 0

if jumlah_anak >= 2 :
    tunjangan = 10/100
else:
    tunjangan = 0

total_pajak = gaji*pajak
G_pajak = gaji-total_pajak
total_tunjangan = gaji*tunjangan
gaji_bersih = pajak +total_tunjangan

print("pekerjaan",pekerjaan)
print("total pajak anda adalah Rp:",total_pajak)
print("total tunjangan anda adalah Rp:",total_tunjangan)
print("gaji bersih selama sebulan Rp:",gaji_bersih)
