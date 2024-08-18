# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # If the value is equal to the root's value, return the root
        if root.val == val:
            return root
        
        # If the value is less than the root's value, search in the left subtree
        elif val < root.val:
            return self.searchBST(root.left, val)
        
        # If the value is greater than the root's value, search in the right subtree
        else:
            return self.searchBST(root.right, val)
