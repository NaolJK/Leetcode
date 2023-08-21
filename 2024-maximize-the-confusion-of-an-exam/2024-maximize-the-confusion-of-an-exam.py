class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        Count = defaultdict(int)
        ans = 0
        
        for right in range(len(answerKey)):
            
            Count[answerKey[right]]+=1
            
            while left <= right and min(Count['T'], Count['F']) > k:
                Count[answerKey[left]]-=1
                left+=1
            
            mxm = right - left + 1
            ans = max(mxm, ans)
        
        return ans
        