"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = Node(-1, [])
        nodes = {}
        if not node: return None

        def dfs(node, prev):
            curr = None
            if node.val in nodes:
                prev.neighbors.append(nodes[node.val])
                return
            else:
                curr = Node(node.val, [])
                prev.neighbors.append(curr)
                nodes[node.val] = curr

            for neighbor in node.neighbors:
                dfs(neighbor, curr)
        
        dfs(node, res)

        return res.neighbors[0]
            