class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# Example usage:
# Example 1:
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(levelOrder(root1))  # Output: [[3], [9, 20], [15, 7]]

# Example 2:
root2 = TreeNode(1)
print(levelOrder(root2))  # Output: [[1]]

# Example 3:
root3 = None
print(levelOrder(root3))  # Output: []
