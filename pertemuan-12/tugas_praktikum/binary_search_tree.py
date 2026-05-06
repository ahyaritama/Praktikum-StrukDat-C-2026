class Book:
    def __init__(self, book_id: int, book_title: str):
        self.id = book_id
        self.title = book_title
        self.left: Book = None
        self.right: Book = None
    
class Library:
    def __init__(self):
        self.root: Book = None
    
    def insert(self, book_id: int, book_title: str):
        if self.root is None:
            self.root = Book(book_id, book_title)
        
        self.__insert(self.root, book_id, book_title)
        print(f"[INSERT] Berhasil memasukkan: ID {book_id} - {book_title}")

    def search(self, book_id: int) -> Book:
        print(f"[SEARCH] Mencari ID {book_id}...", end=" ")
        result = self.__search(self.root, book_id)
        if result:
            print("Ditemukan! Judul:", result.title)
        else:
            print("Data tidak ditemukan.")
        return result

    def traversal_inorder(self) -> list:
        result = self.__traversal_inorder(self.root)
        print("[INFO] Koleksi Buku (In-Order Traversal):")
        
        for i, v in enumerate(result, 1):
            print(f"{i}. {v[0]} - {v[1]}")
        return result

    def get_min(self) -> Book:
        current = self.root
        while current.left:
            current = current.left
        
        print("[STATISTIK] ID Terkecil:", current.id)
        return current

    def get_max(self) -> Book:
        current = self.root
        while current.right:
            current = current.right
        
        print("[STATISTIK] ID Terbesar:", current.id)
        return current

    def height(self) -> int:
        h = self.__height(self.root)
        print("[INFO] Tinggi (Height) Tree:", h)
        return h


    # PRIVATE FUNCTION
    def __insert(self, parent: Book, book_id: int, book_title: str) -> Book:
        if parent is None:
            return Book(book_id, book_title)
        
        if book_id < parent.id:
            parent.left = self.__insert(parent.left, book_id, book_title)
        elif book_id > parent.id:
            parent.right = self.__insert(parent.right, book_id, book_title)
        return parent
    
    def __search(self, parent: Book, book_id: int) -> Book:
        if parent is None:
            return None
        elif parent.id == book_id:
            return parent
        elif book_id < parent.id:
            return self.__search(parent.left, book_id)
        elif book_id > parent.id:
            return self.__search(parent.right, book_id)

    def __traversal_inorder(self, parent: Book, result: list = []) -> list:
        if parent:
            self.__traversal_inorder(parent.left, result)
            result.append((parent.id, parent.title))
            self.__traversal_inorder(parent.right, result)
        return result
    
    def __height(self, parent: Book) -> int:
        if parent is None:
            return -1
        else:
            left = self.__height(parent.left)
            right = self.__height(parent.right)
            return 1 + max(left, right)
        

def main():
    print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
    print("=========================================")
    lib = Library()

    lib.insert(50, "Dasar Pemrograman")
    lib.insert(30, "Struktur Data")
    lib.insert(70, "Kecerdasan Buatan")
    lib.insert(20, "Matematika Diskrit")
    lib.insert(40, "Basis Data")
    lib.insert(60, "Jaringan Komputer")
    lib.insert(80, "Sistem Operasi")
    
    print()
    lib.traversal_inorder()

    print()
    lib.search(60)
    lib.search(100)

    print()
    lib.get_min()
    lib.get_max()
    lib.height()

    print("=========================================")
    print("Simulasi Selesai!")


if __name__ == "__main__":
    main()