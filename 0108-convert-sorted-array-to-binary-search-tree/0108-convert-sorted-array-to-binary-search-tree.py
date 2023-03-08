class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def insert(left,right):
            if left > right:
                return None
            
            mid = (left + right)//2
            new_node = TreeNode(nums[mid])
            new_node.left  = insert(left,mid-1)
            new_node.right = insert(mid+1,right)
            
            return new_node
        return insert(0,len(nums)-1)