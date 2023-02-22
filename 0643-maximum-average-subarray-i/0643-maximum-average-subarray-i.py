class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #initalizing left window as 0start
        left_window = 0
        ans = float("-inf")
        tot = 0
        
        for i in range(len(nums)):
            #summing all elements until it reaches to k 
            tot += nums[i]
            # compare the right window if it reaches greater than k
            if i >=k-1:
                #if it reaches k take the average and compare it with answer
                ans = max(ans,tot/k)
                tot -= nums[left_window]
                left_window += 1
        return ans
        