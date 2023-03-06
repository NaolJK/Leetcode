class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i,word in enumerate(words):
            words[i] = word.count(min(word))
        words.sort()
        
        ans = []
        
        for q in queries:
            count = q.count(min(q))
            res = bisect_right(words,count)
            ans.append(len(words) - res)
            
        return ans