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
    
    def tampilkan_maju(self):
        print("[Maju]")
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print()
    
    def tampilkan_mundur(self):
        current = self.head
        while current and current.next:
            current = current.next
        
        print("[Mundur]")
        while current:
            print(current.data)
            current = current.prev
        print()


def main():
    parkir = ParkirDuaArah()
    parkir.tambah_kendaraan("B 1234 ABC")
    parkir.tambah_kendaraan("D 5678 XYZ")
    parkir.tambah_kendaraan("A 9999 TUV")
    parkir.tampilkan_maju()
    parkir.tampilkan_mundur()


if __name__ == "__main__":
    main()