# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current = headA
        current_two = headB
        
        list_one = set()
        while current != None:
            list_one.add(current)
            current = current.next
        
        # print(list_one)
        while current_two != None:
            if current_two in list_one:
                return current_two
            current_two = current_two.next
        
        return None
            
        