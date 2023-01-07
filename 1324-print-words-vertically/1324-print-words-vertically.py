import itertools

class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        ans = ""
        for string in itertools.zip_longest(*s.split(), fillvalue=" "):
            yield "".join(string).rstrip()
        
        