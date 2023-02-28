# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        right = root.right
        left = root.left
        if not right and not left:
            return True
        if not right or not left:
            return False
        
        r = deque([right])
        l = deque([left])
        
        while r and l:
            r_node = r.popleft()
            l_node = l.popleft()
            if r_node and l_node:
                if r_node.val != l_node.val:
                    return False
                if r_node.right and not l_node.left:
                    return False
                if l_node.left and not r_node.right:
                    return False
                if l_node.right and not r_node.left:
                    return False
                if r_node.left and not l_node.right:
                    return False

                l.append(l_node.left)
                r.append(r_node.right)
                l.append(l_node.right)
                r.append(r_node.left)
        return True
        