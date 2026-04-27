class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def traversalAndPrint(head: Node):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def findLowestValue(head: Node):
    minValue = head.data
    currentNode = head
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

def deleteSpecificNode(head: Node, nodeToDelete: Node):
    if head == nodeToDelete:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next
    
    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next
    return head

def insertNodeAtPosition(head: Node, newNode: Node, position: int):
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(122)
node2 = Node(421)
node3 = Node(135)
node4 = Node(57587)
node5 = Node(243)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traversalAndPrint(node1)
print(findLowestValue(node1))
node1 = deleteSpecificNode(node1, node1)
traversalAndPrint(node1)
print(findLowestValue(node1))
node6 = Node(112)
