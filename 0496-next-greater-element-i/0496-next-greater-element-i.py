class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        stack = []
        final = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                result[stack.pop()] = num
            
            stack.append(num)
            
        for num in nums1:
            if num in result.keys():
                final.append(result[num])
            else:
                final.append(-1)
        return (final)