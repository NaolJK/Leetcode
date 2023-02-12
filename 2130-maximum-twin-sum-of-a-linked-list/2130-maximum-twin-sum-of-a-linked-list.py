# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        while(head):
            nums.append(head.val)
            head = head.next
            
        i = 0
        right = len(nums)-1
        
        maximum = 0
        
        while(i<right):
            if nums[i]+nums[right]>maximum:
                maximum = nums[i]+nums[right]
            i+=1
            right-=1
            
        return maximum 