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
        if not node: return None
        visited = {}
        head = Node(-1, [])

        def dfs(node, prev):
            if node.val in visited:
                prev.neighbors.append(visited[node.val])
                return
            new = Node(node.val, [])
            visited[node.val] = new
            prev.neighbors.append(new)

            for neighbor in node.neighbors:
                dfs(neighbor, new)
                
        dfs(node, head)
        return head.neighbors[0]

