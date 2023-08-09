class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
       
        childs = set(leftChild + rightChild)
        
        root = 0
        
        
        for i in range(n):
            if i not in childs:
                root = i
                break
        
        visited = []
        
        queue = [root]
        
        while queue:
            ele = queue.pop(0)
            if ele in visited:
                return False
            
            visited.append(ele)
            if leftChild[ele] != -1:
                queue.append(leftChild[ele])
                
            if rightChild[ele] != -1:
                queue.append(rightChild[ele])
                
        return len(visited) == n
                
        