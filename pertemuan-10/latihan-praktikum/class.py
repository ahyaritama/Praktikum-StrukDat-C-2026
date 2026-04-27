class RiwayatNavigasi:
    def __init__(self):
        self.items = []
    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def visit(self, url):
        self.push(url)

    def back(self):
        self.pop()
        return self.peek()


def main():
    browser = RiwayatNavigasi()
    browser.visit("https://www.google.com")
    browser.visit("https://classroom.google.com")
    browser.visit("https://www.w3schools.com")
    browser.visit("https://drive.google.com")
    browser.visit("https://classroom.google.com")
    print(browser.items)
    print(browser.size())

    browser.back()
    print(browser.items)

    print(browser.peek())
    print(browser.size())



if __name__ == "__main__":
    main()