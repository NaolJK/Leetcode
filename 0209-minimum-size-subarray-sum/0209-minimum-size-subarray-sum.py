class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left=0
        right=0
        res =0,0,float('inf')
        total=0
        while right<len(nums):
            if total<s:
                total += nums[right]
                right+=1
        
            while total >= s:
                if right -left <res[2]-res[1]:
                    res = total,left,right
                total -= nums[left]
                left+=1
        
        if res[0]==0: 
            return 0
        return res[2]-res[1]
        