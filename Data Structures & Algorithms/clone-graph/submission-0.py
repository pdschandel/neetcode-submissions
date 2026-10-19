from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in cloned:
                return cloned[curr]

            # 1. Create the clone and register it immediately to handle cycles
            copy = Node(curr.val)
            cloned[curr] = copy

            # 2. Populate neighbors recursively
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)