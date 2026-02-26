data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for i in data_aktivitas:
    if i[1] > 80:
        print(f"{i[0]} mendapatkan predikat Gold")
    elif i[1] <= 80 and i[1] >= 50:
        print(f"{i[0]} mendapatkan predikat Silver")
    else:
        print(f"{i[0]} mendapatkan predikat Bronze")