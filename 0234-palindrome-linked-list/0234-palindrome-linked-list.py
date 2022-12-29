# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        fast = head 
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if not slow.next:
            return head.val == slow.val
            
        middle = slow
        next_pointer = slow.next
        temp = slow.next.next
        
        
        while next_pointer and temp:
            next_pointer.next = slow
            slow = next_pointer
            next_pointer = temp
            temp = temp.next
        
        next_pointer.next = slow
        middle.next = None
        start = head 
        end = next_pointer 
        
        while start and end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next 
        
        return True

        