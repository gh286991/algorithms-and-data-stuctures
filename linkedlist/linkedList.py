class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(1)
    def insertStart(self,data):
        self.size = self.size +1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self,data):

        if self.head is None:
            return

        currentNode = self.head
        previousNode = None
        
        while currentNode.data != data:
            previousNode = currentNode
            if currentNode.nextNode is None:
                    return #when you dont find the data then just exist as current.next will be null. bug fix 2
            else:
                currentNode = currentNode.nextNode

        self.size = self.size -1 

        previousNode.nextNode = currentNode.nextNode


    #  O(1)
    def size(self):
        return self.size

    # O(N)
    def size2(self):

        actualNode = self.head
        size = 0
        
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size

    def insertEnd(self,data):
        self.size = self.size +1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d" %actualNode.data, end = ', ')
            actualNode = actualNode.nextNode

linkedlist = LinkedList()

linkedlist.insertStart(12)
linkedlist.insertStart(123)
linkedlist.insertStart(99)
linkedlist.insertEnd(578)
linkedlist.traverseList()
print('-----')
linkedlist.remove(12)
linkedlist.traverseList()
print('-----')
print(linkedlist.size)