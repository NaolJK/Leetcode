# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = None
        # pos = stack.next
        curr = head
        while curr:
            while stack and curr and curr.val > stack.val:
                stack = stack.next    
            new_node = ListNode(curr.val)
            if not stack:
                new_node.next = stack
                stack = new_node
            else:
                new_node.next = stack
                stack = new_node
            curr = curr.next
        
        p1, p2,p3 = None, stack, stack.next
        while p3:
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
       
        p2.next = p1
                
        return p2
            
            
        
        