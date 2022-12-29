# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head 
        stack = []
        
        while curr != None:
            stack.append(curr.val)
            curr = curr.next
        
        def checkPalindrome(stack):
            if len(stack) == 0 or len(stack) == 1:
                return True
        
            left = stack.pop(0)
            right = stack.pop()
            
            
            if left != right:
                return False
            
            return checkPalindrome(stack)
        
        return checkPalindrome(stack)
        