# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        curr = head
        
        while curr:
            prev_curr = dummy
            prev_node = dummy
            next_node = prev_node.next

            while prev_curr and prev_curr.next != curr:
                prev_curr = prev_curr.next

            while next_node != curr:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next
            
            next_iter = curr.next
            if next_node != curr:
                curr.next = next_node
                prev_node.next = curr
                if prev_curr:
                    prev_curr.next = next_iter

            curr = next_iter

        return dummy.next
        