class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        
        threshold = len(nums) // 3
        
        ans = []
        
        for key, v in count.items():
            if v > threshold:
                ans.append(key)
        
        return ans
        
        
        
        
        
        
        