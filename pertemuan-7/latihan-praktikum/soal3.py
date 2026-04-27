class Plat:
    def __init__(self, data):
        self.data = data
        self.next = None

def sisipkan_vip(plat_baru, plat_target):
    plat_baru.next = plat_target.next
    plat_target.next = plat_baru

def tampilkan_antrean(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

plat1 = Plat("BM 1323 RA")
plat2 = Plat("BM 1242 RA")
plat3 = Plat("BM 1125 RA")
plat4 = Plat("BM 7545 RA")

plat1.next = plat2
plat2.next = plat3

tampilkan_antrean(plat1)
sisipkan_vip(plat4, plat2)
tampilkan_antrean(plat1)