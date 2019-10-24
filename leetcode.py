class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def insertStart(self,data):
        self.size = self.size +1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
        
linkedlist = ListNode()
linkedlist.insertStart(2)
linkedlist.insertStart(3)