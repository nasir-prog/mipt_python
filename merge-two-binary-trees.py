from typing import Optional


class Solution:
    def mergeTrees(
        self, root1: Optional["TreeNode"], root2: Optional["TreeNode"]
    ) -> Optional["TreeNode"]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack = [(root1, root2)]
        while stack:
            first, second = stack.pop()
            first.val += second.val
            if first.left is None:
                first.left = second.left
            elif second.left is not None:
                stack.append((first.left, second.left))
            if first.right is None:
                first.right = second.right
            elif second.right is not None:
                stack.append((first.right, second.right))
        return root1
