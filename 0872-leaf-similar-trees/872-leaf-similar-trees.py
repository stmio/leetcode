class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(node):
            if node == None:
                return []
            elif node.left == None and node.right == None:
                return [node.val]
            return leaf(node.left) + leaf(node.right)
        return leaf(root1) == leaf(root2)
        