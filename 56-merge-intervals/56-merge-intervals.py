class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) == 0):
            return intervals
        intervals.sort(key=lambda x:x[0])
        last = intervals[0]
        final_result = []
        for interval in intervals:
            if interval[0] <= last[1]:
                last[1] = max(interval[1],last[1])
            else:
                final_result.append(last)
                last = interval
        final_result.append(last)
        return final_result
                
      
        