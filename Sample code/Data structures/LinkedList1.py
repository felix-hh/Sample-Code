class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext

class linkedList(object):
    def __init__ (self, head=None):
        self.head = head
        
    def insert(self, newNode):
        newNode.setNext(self.head)
        self.head=newNode
        
    def size(self):
        current=self.head
        count = 0
        while current:
            count+=1
            current=current.getNext()
        return count
    
    def search(self, data):
        current=self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:
            raise ValueError ("Nothing here")
        return current

    def delete(self,data):
        current=self.head
        previous=None
        found=False
        while current and found is False:
            if current.getData()==data:
                found = True
            else:
                previous = current
                current=current.getNext
        if current is None:
            raise ValueError("nothing here!")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def read(self):
        current=self.head
        while current is not None:
            print (current.getData())
            current=current.getNext()

newNode=Node("hello")
newNode2=Node("how are you")
lList = linkedList(Node("n-scheme"))
lList.insert(newNode)
lList.insert(Node("cacatuas multiples"))
lList.read()
print(lList.head.getData())
