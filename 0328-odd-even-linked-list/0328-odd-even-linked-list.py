# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd_node = head
        even_node = head.next
        o_head = odd_node
        e_head = even_node
        
        while even_node and even_node.next:
            odd_node.next = even_node.next
            even_node.next = even_node.next.next
            even_node = even_node.next
            odd_node = odd_node.next
            
        odd_node.next = e_head
        
        return o_head
        
            
        