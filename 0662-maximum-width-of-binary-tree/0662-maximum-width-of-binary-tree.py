# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([])
        queue.append((root,0,0))
        ans = defaultdict(list)
        
        while queue:
            node, row, col = queue.popleft()
            ans[row].append((col, node.val))
            
            if node.left:
                queue.append((node.left, row+1 ,2*(col)+1))
             
            if node.right:
                queue.append((node.right, row+1, 2*(col)+2))
        
        maximum_area = 0
        # print(ans)
        for key, value in ans.items():
            w = sorted(value)
            width = w[-1][0] - w[0][0] + 1
            # print(width , w)
            maximum_area = max(maximum_area , width)
            
        return (maximum_area)
       
            
                
            
        