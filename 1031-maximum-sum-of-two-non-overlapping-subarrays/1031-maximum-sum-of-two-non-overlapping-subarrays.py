from collections import deque

class Solution:
    def slidingWindows(self, A: List[int], L: int, M: int) -> int:
        # Create deques and starting sums for the 'l' and 'm' sliding windows
        lQ = deque(maxlen=L)
        mQ = deque(maxlen=M)
        lSum = 0
        mSum = 0
        
        # Fill deques and sums with their appropriate starter values, l then m
        for i in range(L):
            lQ.append(A[i])
            lSum += A[i]
            
        for j in range(i+1, i+1+M):
            mQ.append(A[j])
            mSum += A[j]
            
        # Slide windows, retaining the max sums for the left (l) deque and overall
        maxLSum = lSum
        maxOverall = maxLSum + mSum
        for k in range(j+1, len(A)):
            # Shift the leftmost elem from mQ into lQ and the next elem into mQ
            shiftedFromM = mQ.popleft()
            shiftedFromL = lQ.popleft()
            lQ.append(shiftedFromM)
            mQ.append(A[k])
            
            # Update the deque sums to account for the shifts in and out
            lSum = lSum - shiftedFromL + shiftedFromM
            mSum = mSum - shiftedFromM + A[k]
            
            # Update the max sums for the left deque and overall
            maxLSum = max(maxLSum, lSum)
            maxOverall = max(maxOverall, maxLSum + mSum)
            
        return maxOverall
        
        
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
	    # Take the best result of the two possible orders for the l and m windows
        return max(self.slidingWindows(A, L, M), self.slidingWindows(A, M, L))