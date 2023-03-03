# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            res = isBadVersion(mid)
            if not res:
                start = mid + 1
            else:
                end = mid - 1
                
        return start