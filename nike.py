import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

penjualan_hitam = [900, 975, 1150, 1325, 1500, 1675, 1850, 2025, 2200, 2375, 2550, 2725]
penjualan_putih = [1500, 1100, 1200, 1300, 1400, 1450, 1350, 1200, 1050, 900, 750, 600]
penjualan_biru = [1000, 750, 725, 710, 700, 775, 720, 710, 760, 740, 730, 705]


harga_sepasang = 100000
produksi_target = {'hitam': 21500, 'putih': 15000, 'biru': 13500}
biaya_total = 5000000000


total_penjualan_hitam = sum(penjualan_hitam)
total_penjualan_putih = sum(penjualan_putih)
total_penjualan_biru = sum(penjualan_biru)


pendapatan_hitam = total_penjualan_hitam * harga_sepasang
pendapatan_putih = total_penjualan_putih * harga_sepasang
pendapatan_biru = total_penjualan_biru * harga_sepasang
total_pendapatan = pendapatan_hitam + pendapatan_putih + pendapatan_biru


persentase_penjualan_hitam = (total_penjualan_hitam / produksi_target['hitam']) * 100
persentase_penjualan_putih = (total_penjualan_putih / produksi_target['putih']) * 100
persentase_penjualan_biru = (total_penjualan_biru / produksi_target['biru']) * 100


keuntungan = total_pendapatan - biaya_total


print("Laporan Penjualan Bulanan per Warna:")
print("Penjualan warna hitam:", penjualan_hitam)
print("Penjualan warna putih:", penjualan_putih)
print("Penjualan warna biru:", penjualan_biru)


print("\nLaporan Persentase Penjualan Terhadap Target Produksi per Warna:")
print(f"Persentase penjualan warna hitam: {persentase_penjualan_hitam:.2f}% dari target")
print(f"Persentase penjualan warna putih: {persentase_penjualan_putih:.2f}% dari target")
print(f"Persentase penjualan warna biru: {persentase_penjualan_biru:.2f}% dari target")


print("\nLaporan Keuntungan Penjualan:")
print(f"Pendapatan total warna hitam: Rp {pendapatan_hitam}")
print(f"Pendapatan total warna putih: Rp {pendapatan_putih}")
print(f"Pendapatan total warna biru: Rp {pendapatan_biru}")
print(f"Total pendapatan: Rp {total_pendapatan}")
print(f"Biaya produksi total: Rp {biaya_total}")
print(f"Keuntungan bersih: Rp {keuntungan}")


bulan = range(1, 13)
plt.plot(bulan, penjualan_hitam, label='Hitam', marker='o')
plt.plot(bulan, penjualan_putih, label='Putih', marker='o')
plt.plot(bulan, penjualan_biru, label='Biru', marker='o')
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penjualan")
plt.title("Grafik Penjualan Sepatu Niki per Bulan Berdasarkan Warna")
plt.legend()
plt.grid(True)
plt.show()
