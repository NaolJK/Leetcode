# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = [] 
        stack = []
        
        count = 0
        
        while head != None:
            while stack and stack[-1][0] < head.val:
                result[stack[-1][1]] = head.val
                stack.pop()
                
            stack.append([head.val,count])
            result.append(0)
            count+=1 
            head = head.next
            
        return (result)
        
        
        
            
                
        