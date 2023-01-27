class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None
        
        
class MyLinkedList:

    def __init__(self):
        self.head = None
    


    def get(self, index: int) -> int:
        curr = self.head 
        i = 0
        while i < index and curr:
            curr = curr.next
            i+=1
        if curr:
             return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
     
        
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.head
        if not self.head:
            self.head = new_node 
            return
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        

        
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        if index == 0:
            self.addAtHead(val)
            return

        i = 0
        while curr and i < index-1:
            curr = curr.next
            i+=1
        if not curr:
            return 
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if index == 0:
            self.head = self.head.next
            return 

        i = 0
        while curr and i < index-1:
            curr = curr.next
            i+=1
        if curr and curr.next:
            curr.next = curr.next.next
        return 
        
        
        
        
        

        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)