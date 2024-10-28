harga_sepatu = 100000 
total_produksi = 50000  
stok_awal = {
    "hitam": 21500,
    "putih": 15000,
    "biru": 13500
}


penjualan = {
    "hitam": [900, 975, 1150, 1325, 1500, 1675, 1850, 2025, 2200, 2375, 2550, 2725],
    "putih": [1500, 1100, 1200, 1300, 1400, 1450, 1350, 1200, 1050, 900, 750, 600],
    "biru": [1000, 750, 725, 710, 700, 775, 720, 710, 760, 740, 730, 705]
}

def hitung_total_penjualan(penjualan_bulanan):
    return sum(penjualan_bulanan)


def hitung_pendapatan(total_penjualan, harga_per_unit):
    return total_penjualan * harga_per_unit


def hitung_sisa_stok(stok_awal, total_terjual):
    return stok_awal - total_terjual


hasil_analisis = {}
total_pendapatan = 0  
for warna, data_penjualan in penjualan.items():
    total_terjual = hitung_total_penjualan(data_penjualan)
    pendapatan = hitung_pendapatan(total_terjual, harga_sepatu)
    sisa_stok = hitung_sisa_stok(stok_awal[warna], total_terjual)
    
    hasil_analisis[warna] = {
        "total_terjual": total_terjual,
        "pendapatan": pendapatan,
        "sisa_stok": sisa_stok
    }
    total_pendapatan += pendapatan  


print("Hasil Analisis Penjualan Sepatu Niki")
print("====================================")
for warna, data in hasil_analisis.items():
    print(f"Warna {warna.capitalize()}:")
    print(f"  Total Terjual: {data['total_terjual']} pasang")
    print(f"  Pendapatan   : Rp {data['pendapatan']}")
    print(f"  Sisa Stok    : {data['sisa_stok']} pasang")
    print("------------------------------------")


print(f"\nTotal Pendapatan Seluruh Penjualan: Rp {total_pendapatan}")