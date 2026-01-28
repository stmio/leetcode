# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = [(root, 0)]
        res = []

        while queue:
            x, depth = queue.pop(0)

            if x.left:
                queue.append((x.left, depth + 1))
            if x.right:
                queue.append((x.right, depth + 1))

            if len(res) <= depth:
                res.append([])
            
            res[depth].append(x.val)

        return res
            


