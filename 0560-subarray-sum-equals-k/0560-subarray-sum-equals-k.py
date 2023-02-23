class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))
        prefix.insert(0,0)
        result = 0
        count = {}
        
        for idx,num in enumerate(prefix):
            
            if prefix[idx]-k in count:
                result = result + count[prefix[idx]-k]
                
            if prefix[idx] in count:
                count[prefix[idx]]+=1
            else:
                count[prefix[idx]] = 1
        return result