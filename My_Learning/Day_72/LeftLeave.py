class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    if not root:
        return 0
    
    def is_leaf(node):
        return node and not node.left and not node.right
    
    def dfs(node):
        total_sum = 0
        if node.left:
            if is_leaf(node.left):  # Check if left child is a leaf
                total_sum += node.left.val
            else:
                total_sum += dfs(node.left)  # Traverse left subtree
        if node.right:
            total_sum += dfs(node.right)  # Traverse right subtree
        return total_sum
    
    return dfs(root)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sumOfLeftLeaves(root))  # Output: 24 (9 + 15)
