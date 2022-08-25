#link in the start
class Node(object):
    
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
class LinkList(object):
    #head node
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(f'{temp.data}->',end="")
            temp = temp.next
        print('Null')
    #new node
    def insertAtStart(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            
if __name__ == "__main__":
    List = LinkList()
    List.insertAtStart(5)
    List.insertAtStart(10)
    List.insertAtStart(11)
    
    List.printList()


#Link in the end
class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
class LinkList(object):
    def __init__(self):
        self.head= None
    def printList(self):
        temp = self.head
        while(temp):
            print(f'{temp.data}->',end=" ")
            temp = temp.next
        print("NULL")
    def insertAtStart(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    def insertAtEnd(self,data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        
if __name__ == "__main__":
    List = LinkList()
    List.head = Node(1)
    List.insertAtEnd(5)
    List.insertAtEnd(10)
    List.insertAtEnd(15)
    List.printList()


#Link insert between
class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def setNext(self,next):
        self.next = next
        
class LinkList(object):
    def __init__(self):
        self.head= None
    def printList(self):
        temp = self.head
        while(temp):
            print(f'{temp.data}->',end=" ")
            temp = temp.next
        print("NULL")
    def insertAtStart(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            
    def insertAtEnd(self,data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        
    def insertAtBetween(self, previousNode, data):
        if previousNode.next is None:
            print("Previous node con't be none")
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode
        
if __name__ == "__main__":
    List = LinkList()
    List.head = Node(10)
    node2 = Node(2)
    List.head.setNext(node2)
    node3 = Node(35)
    node2.setNext(node3)
    List.insertAtBetween(node2, 45)
    List.insertAtEnd(6)
    List.printList()
