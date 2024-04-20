class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    def is_valid(node, min_val, max_val):
        if not node:
            return True
        
        # Check if the current node's value is within the valid range
        if not (min_val < node.val < max_val):
            return False
        
        # Recursively check the left subtree and right subtree
        return (is_valid(node.left, min_val, node.val) and 
                is_valid(node.right, node.val, max_val))
    
    # Use a helper function to check the validity with initial range of (-inf, +inf)
    return is_valid(root, float('-inf'), float('inf'))

# Test cases
# Example 1: [2,1,3]
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(is_valid_bst(root1))  # Output: True

# Example 2: [5,1,4,null,null,3,6]
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(is_valid_bst(root2))  # Output: False
