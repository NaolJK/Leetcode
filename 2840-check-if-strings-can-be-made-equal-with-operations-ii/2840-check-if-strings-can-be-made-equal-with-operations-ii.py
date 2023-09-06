class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        g1 = []
        g2 = []
        g3 = []
        g4 = []
        
        for i in range(0,len(s1), 2):
            g1.append(s1[i])
            
        for i in range(1,len(s1), 2):
            g2.append(s1[i])
        
        for i in range(0,len(s1), 2):
            g3.append(s2[i])
            
        for i in range(1,len(s1), 2):
            g4.append(s2[i])
        
        g1.sort()
        g2.sort()
        g3.sort()
        g4.sort()
        
        g1 = "".join(g1)
        g2 = "".join(g2)
        g3 = "".join(g3)
        g4 = "".join(g4)
        
        return (g1 == g3) and (g2 == g4)