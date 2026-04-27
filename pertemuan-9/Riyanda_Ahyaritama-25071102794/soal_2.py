class Node:
    def __init__(self, data):
        self.prev: Node = None
        self.next: Node = None
        self.data = data

class ParkirDuaArah:
    def __init__(self):
        self.head: Node = None
    
    def tambah_kendaraan(self, plat):
        if self.head is None:
            self.head = Node(plat)
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(plat)
        current.next.prev = current
    
    def hapus_kendaraan(self, plat):
        current = self.head
        while current:
            if current.data == plat:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return
            current = current.next

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print()
    
    def tampilkan_mundur(self):
        current = self.head
        while current and current.next:
            current = current.next
        
        while current:
            print(current.data)
            current = current.prev
        print()


def main():
    parkir = ParkirDuaArah()
    parkir.tambah_kendaraan("B 1111 AA")
    parkir.tambah_kendaraan("D 2222 BB")
    parkir.tambah_kendaraan("A 3333 CC")
    parkir.tambah_kendaraan("B 4444 DD")

    print("Sebelum:")
    parkir.tampilkan_maju()
    parkir.hapus_kendaraan("A 3333 CC")

    print("Sesudah:")
    parkir.tampilkan_maju()


if __name__ == "__main__":
    main()