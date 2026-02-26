ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

only_coding = ukm_coding - ukm_robotik
print(only_coding)

ukm_union = ukm_coding | ukm_robotik
print(ukm_union)

isMember = False
for x in ukm_robotik:
    if x == "Andi":
        isMember = True

print(isMember)