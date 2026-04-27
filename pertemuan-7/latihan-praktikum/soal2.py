class Plat:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def cekKendaraan(head: Plat):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def tambahKendaraan(head: Plat, plat: Plat):
    currentNode = head
    while currentNode.next:
        currentNode = currentNode.next

    currentNode.next = plat

def hapusKendaraan(head: Plat, plat: Plat):
    if head == plat:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next != plat:
        currentNode = currentNode.next
    
    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next
    return head

plat1 = Plat("BM 1323 RA")
plat2 = Plat("BM 1242 RA")
plat3 = Plat("BM 1125 RA")
plat4 = Plat("BM 7545 RA")

plat1.next = plat2
plat2.next = plat3

cekKendaraan(plat1)
tambahKendaraan(plat1, plat4)
cekKendaraan(plat1)
plat1 = hapusKendaraan(plat1, plat3)
cekKendaraan(plat1)
