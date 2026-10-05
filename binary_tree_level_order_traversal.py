from collections import deque
from typing import Optional


class Solution:
    def levelOrder(self, root: Optional["TreeNode"]) -> list[list[int]]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
        return result
