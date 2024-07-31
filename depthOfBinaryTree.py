class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        height = 1
        node = root
        left = node.left
        right = node.right
        if left is not None or right is not None:
            height = height + 1
        
        node = right
        left = node.left
        right = node.right
        if left is not None or right is not None:
            height = height + 1
        
        node = left
        left = node.left
        right = node.right
        if left is not None or right is not None:
            height = height + 1
                
        return height


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

