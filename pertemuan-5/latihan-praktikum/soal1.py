stok_barang = [15, 40, 30, 10, 25]

index_10 = stok_barang.index(10)
stok_barang[index_10] = 50

stok_barang.append(5)
print(stok_barang)

stok_barang.sort(reverse=True)
print(stok_barang)

jumlah = sum(stok_barang)
print(jumlah)
print("Stok Aman" if jumlah/len(stok_barang) > 20 else "Waspada")