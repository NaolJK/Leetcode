class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #initialize a count of every modulo in the list
        count = defaultdict(int)
        result = 0
        
        
        count[0] = 1
        total_sm = 0
        for i, num in enumerate(nums):
            total_sm+=num
            mod = total_sm%k
            result+=count[mod]
            count[mod]+=1
            
        return result
            
            
            