class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        pre_calculated = self.getRow(rowIndex-1)
        ans = [1]
        
        for i in range(1,rowIndex):
            res = pre_calculated[i] + pre_calculated[i-1]
            ans.append(res)
            
        ans.append(1)
        
        return ans
            