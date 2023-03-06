class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isPossible(n):
            ans = 0
            for num in nums:
                res = ceil(num/n)
                ans+=res
            # print(n,ans)
            return ans
        left,right = 1 , max(nums)
        # print("left",left,right)
        while left < right:
            middle = (left+right)//2
            res = isPossible(middle)
            
            if res > threshold:
                left = middle + 1
            else:
                right = middle
                
        return (right)
            
                
            