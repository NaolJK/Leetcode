class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        
        for index, elem in enumerate(nums):
            if target-elem in counter:
                return counter[target-elem], index
            
            counter[elem] = index
                
        