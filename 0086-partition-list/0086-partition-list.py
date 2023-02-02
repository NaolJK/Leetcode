# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        prev = head
        greater = ListNode()
        dummy = greater
        
        while curr:
            if curr.val < x:
                if curr == prev:
                    
                    prev = prev.next
                    head = prev
                    dummy.next = curr
                    curr.next = None
                    dummy = dummy.next
                    curr = prev
                else:
                    prev.next = curr.next
                    dummy.next = curr
                    dummy = dummy.next
                    curr.next = None
                    curr = prev
            else:
                if curr == prev:
                    curr = curr.next
                else:
                    curr = curr.next
                    prev = prev.next
        dummy.next = head
        
        return greater.next
    
            
        
                    
        