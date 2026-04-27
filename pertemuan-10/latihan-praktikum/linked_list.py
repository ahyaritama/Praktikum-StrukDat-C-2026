class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class RiwayatNavigasiLinkedList:
    def __init__(self):
        self.top: Node = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        return self.size == 0

    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return
        
        url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return url

    def peek(self):
        if self.is_empty():
            return
        return self.top.url

    def size(self):
        return self.count
    
    def traverse_and_print(self):
        current = self.top
        while current:
            print(current.url, end=" -> ")
            current = current.next
        print("None")

    def visit(self, url):
        self.push(url)

    def back(self):
        self.pop()
        return self.peek()


def main():
    browser = RiwayatNavigasiLinkedList()
    browser.visit("https://www.google.com")
    browser.visit("https://classroom.google.com")
    browser.visit("https://www.w3schools.com")
    browser.visit("https://drive.google.com")
    browser.visit("https://classroom.google.com")
    browser.traverse_and_print()
    print(browser.size())

    browser.back()
    browser.traverse_and_print()

    print(browser.peek())
    print(browser.size())



if __name__ == "__main__":
    main()