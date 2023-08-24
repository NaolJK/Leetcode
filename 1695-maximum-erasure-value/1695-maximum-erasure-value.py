class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        elem = defaultdict(int)
        left = mx = 0
        
        lcl = 0
        for right in range(len(nums)):
            
            lcl += nums[right]
            elem[nums[right]]+=1
            
            while left <= right and elem[nums[right]] > 1:
                # print(elem, nums[left:right+1])
                elem[nums[left]] -= 1
                lcl-=nums[left]
                left+=1
            
            mx = max(mx , lcl)
        
        return mx
            
            