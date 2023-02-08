# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(None)
        pos = ans
        
        curr_1 = l1
        curr_2 = l2
        carry = 0
        while curr_1 and curr_2:
            num1 = curr_1.val
            num2 = curr_2.val
            summation = num1 + num2 + carry
            carry = summation // 10
            res = summation%10
            new_node = ListNode(res)
            pos.next = new_node
            pos = new_node
            curr_1 = curr_1.next
            curr_2 = curr_2.next
        
        while curr_1:
            summation = curr_1.val + carry
            carry = summation//10
            res = summation % 10
            new_node = ListNode(res)
            pos.next = new_node
            pos = new_node
            curr_1 = curr_1.next
            
        while curr_2:
            summation = curr_2.val + carry
            carry = summation//10
            res = summation % 10
            new_node = ListNode(res)
            pos.next = new_node
            pos = new_node
            curr_2 = curr_2.next
        
        if carry != 0:
            new_node = ListNode(carry)
            pos.next = new_node
            pos = new_node
        return ans.next
        
        