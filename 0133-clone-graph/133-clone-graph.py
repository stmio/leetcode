"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def traverse(node):
            if not node: 
                return None
            if node in old_to_new:
                return old_to_new[node]

            old_to_new[node] = Node(node.val)
            old_to_new[node].neighbors = [traverse(n) for n in node.neighbors]

            return old_to_new[node]

        return traverse(node)