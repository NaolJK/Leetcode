# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ptr = 0
        curr = head 
        while curr:
            curr = curr.next
            ptr+=1
        
        if ptr == 1:
            return head
        
        k = k % ptr
        if k == 0:
            return head
        
        curr = head 
        i  = 0
        end = ptr - k - 1
        while i < end:
            curr = curr.next
            i+=1
        
        h2 = curr.next
        curr.next = None
        
        curr = h2
        while curr and curr.next:
            curr = curr.next
        
        if curr:
            curr.next = head
        return h2
    
        