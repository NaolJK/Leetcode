class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summation = sum([even for even in nums if even%2==0])
        stack = []
        
        for value,index in queries:
            if nums[index] % 2 == 0:
                summation -= nums[index]
                
            nums[index] += value
            
            if nums[index] % 2 == 0:
                summation+=nums[index]
            
            stack.append(summation)
        
        return (stack)
        