# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        j =1
        queue = deque([(root, 1)])
        ans = defaultdict(list)

        while queue:
            node, level = queue.popleft()
            ans[level].append(node.val)
            if node:
                if node.right:
                    queue.append((node.right, level+1))
                if node.left:
                    queue.append((node.left,level+1))
        ans =  (list(ans.values()))
        i = 2
        while i < len(ans):
            ans[i] = ans[i][::-1]
            i+=2
        return ans
        
            
                        
        