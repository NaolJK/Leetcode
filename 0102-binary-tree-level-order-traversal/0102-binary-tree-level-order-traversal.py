# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 1)])
        ans = defaultdict(list)
        while queue:
            node, level  = queue.popleft()
            ans[level].append(node.val)
            if node:
                if node.left:
                    queue.append((node.left,level+1))
                if node.right:
                    queue.append((node.right,level+1))
        return (list(ans.values()))
                    
                    
        