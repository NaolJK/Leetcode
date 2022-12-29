# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        if not head.next.next:
            return head.val == head.next.val
        
        fast = head 
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
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
        print(end.next.val)
        
        def checkPalindrome(start,end):
            if not (start and end):
                return True
            if start and start.val != end.val:
                return False
            
            return checkPalindrome(start.next,end.next)
        return checkPalindrome(start,end)
        
            
            
        
        
#         curr = head 
#         stack = []
        
#         while curr != None:
#             stack.append(curr.val)
#             curr = curr.next
        
#         def checkPalindrome(stack):
#             if len(stack) == 0 or len(stack) == 1:
#                 return True
            
#             left = stack.pop(0)
#             right = stack.pop()
            
#             if left != right:
#                 return False
            
#             return checkPalindrome(stack)
        
#         return checkPalindrome(stack)
        