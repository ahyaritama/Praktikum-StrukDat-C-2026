class Node:
    def __init__(self, data):
        self.next: Node = None
        self.data = data

class GiliranPetugasValet:
    def __init__(self):
        self.head: Node = None
    
    def tambah_petugas(self, nama):
        if self.head is None:
            self.head = Node(nama)
            self.head.next = self.head
            return
        
        current = self.head
        while current.next is not self.head:
            current = current.next
        
        current.next = Node(nama)
        current.next.next = self.head
    
    def giliran_berikutnya(self, n):
        if self.head is None:
            return
        
        current = self.head
        for i in range(n):
            print(f"Giliran {i + 1}: {current.data}")
            current = current.next


def main():
    valet = GiliranPetugasValet()
    valet.tambah_petugas("Andi")
    valet.tambah_petugas("Budi")
    valet.tambah_petugas("Citra")
    valet.tambah_petugas("Dewi")
    valet.giliran_berikutnya(6)

if __name__ == "__main__":
    main()