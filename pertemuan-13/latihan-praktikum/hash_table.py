class BookData:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def insert(self, book_code, book_title):
        index = self.__hash_function(book_code)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == book_code:
                bucket[i] = (book_code, book_title)
                print(f"Data with key '{book_code}' successfully updated")
                return
        
        bucket.append((book_code, book_title))
        print(f"Data '{book_code} : {book_title}' successfully added")

    def search(self, book_code):
        index = self.__hash_function(book_code)
        bucket = self.table[index]

        for k, v in bucket:
            if k == book_code:
                return v
        return None

    def delete(self, book_code):
        index = self.__hash_function(book_code)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == book_code:
                del bucket[i]
                print(f"Data with key '{book_code}' successfully deleted")
                return True
            
        return False

    def display(self):
        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")

    def __hash_function(self, key):
        total = 0
        for char in str(key):
            total += ord(char)        
        return total % self.size


def main():
    bd = BookData()

    bd.insert("BK111", "Mahir C++ Dalam Satu Jam")
    bd.insert("BK222", "Python Dasar")
    bd.insert("BK333", "Matematika Diskrit")
    bd.insert("BK444", "Atomic Habits")
    bd.display()

    print()
    bd.insert("BK045", "Mein Kampf")
    bd.insert("BK111", "Bumi Manusia")
    bd.display()

    print()
    print("Book title with code BK045:", bd.search("BK045"))
    print("Book title with code BK026:", bd.search("BK026"))

    print()
    bd.delete("BK333")
    bd.display()
    
if __name__ == "__main__":
    main()