gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]

for x in gudang_pc:
    if x["item"] == "Keyboard":
        x["kategori"] = "Aksesoris"

print(gudang_pc)

gudang_pc.append({
    "item": "Headset",
    "harga": 350000,
    "stok": 8
})

print(gudang_pc)

for x in gudang_pc:
    print(f"Item: {x["item"]} | Total Aset: Rp.{x["stok"] * x["harga"]}")