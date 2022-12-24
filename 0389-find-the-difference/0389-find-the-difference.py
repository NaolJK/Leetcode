class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for elem in t:
            if s.count(elem) != t.count(elem):
                return elem
                
        

        