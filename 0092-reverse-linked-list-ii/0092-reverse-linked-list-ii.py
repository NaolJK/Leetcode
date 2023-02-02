# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head.next:
            return head
        
        current,prev,position = head,None,1
        
        while current.next and position < left:
            prev = current
            current = current.next
            position+=1
        
        previous = prev
        middle = current
        
        while position < right:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
            position+=1
        
        if left == 1:
            head = current
        else:
            previous.next = current
        
        middle.next = current.next
        current.next = prev
        
        return head
        