class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted([[start,end,i] for i, [start,end] in enumerate(intervals)])
        
        
        ans = [-1] * len(intervals)
        
        
        begining_vals = [start for start,end,i in intervals]
        
        for b,e,indx in intervals:
            
            x = bisect.bisect_left(begining_vals, e)
            
            if x != len(begining_vals):
                
                ans[indx] = intervals[x][-1]
        
        return ans