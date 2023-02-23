class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        nums.sort(reverse=True)
        intervals = [0]*(length+1)

        for left, right in requests:
            intervals[left]+=1
            intervals[right+1]-=1
        intervals = list(accumulate(intervals))
        intervals.pop()
        intervals.sort(reverse=True)
        ans = 0
        for idx,interval in enumerate(intervals):
            ans+=(interval*nums[idx])
        return ans % (10**9 + 7)
            
            
        
        
        
        