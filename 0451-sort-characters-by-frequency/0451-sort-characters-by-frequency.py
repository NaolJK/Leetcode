class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        strings = []
        heapify(strings)
        for key, val in cnt.items():
            heappush(strings, (-1*val, key))
        
        ans = ""
        while strings:
            cnt, letter = heappop(strings)
            ans+=(-1*cnt * letter)
        return ans
        
            
        