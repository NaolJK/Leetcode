class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # index = 0
        total = 0
        
        prefix = []
        for c in chalk:
            total += c
            prefix.append(total)
        
        k %= total
        lo, hi = 0, len(prefix) - 1

        while lo <= hi:
            mid = (lo + hi)//2
            if k > prefix[mid]:
                lo = mid + 1
            elif k < prefix[mid]:
                hi = mid - 1
            else:
                return mid + 1

        return lo