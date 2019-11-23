#now lets write the linked list from scratch

class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data=data
        self.nextNode=nextNode
    def getData(self):
        return self.data
    def getNext(self):
        return self.nextNode
    def setNext(self, newNext):
        self.nextNode=newNext

class linkedList(object):
    def __init__(self, head=None):
        self.head=head
    def insert(self, data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            self.head.setNext(newNode)
            self.head=newNode
    def insertNode(self, node):
        if self.head is None:
            self.head=node
        else:
            node.setNext(self.head)
            self.head=node
    def read(self):
        current=self.head
        while current is not None:
            print(current.getData())
            current=current.getNext()

l=linkedList()
for i in range (10):
    l.insertNode(Node(i))

l.read()
    
