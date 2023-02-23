class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]*len(s2)
        s1_count = Counter(s1)
        window = len(s1)-1
        for i,s in enumerate(s2):
            if s in set(s1):
                count[i] = 1
        left = 0
        for right in range(len(s2)):
            if count[right] == 0:
                left+=1

            if right-left == window:
                s2_count = Counter(s2[left:right+1])
                if s1_count == s2_count:
                    return True
                else:
                    left+=1
        return False
            
            
        