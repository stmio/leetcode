# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        def dfs(node_a, node_b):
            if not node_a and not node_b:
                return True
            elif node_a and node_b and node_a.val == node_b.val:
                return dfs(node_a.left, node_b.left) and dfs(node_a.right, node_b.right)
            return False
        
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)