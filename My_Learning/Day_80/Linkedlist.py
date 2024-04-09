class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return
    
    # Recursive function to flatten the subtree rooted at 'node'
    def flattenSubtree(node):
        if not node:
            return None
        
        # Flatten the left and right subtrees recursively
        left_end = flattenSubtree(node.left)
        right_end = flattenSubtree(node.right)
        
        # Save the original right subtree
        right_subtree = node.right
        
        # Make the left subtree the new right subtree
        node.right = node.left
        node.left = None
        
        # Attach the original right subtree to the end of the current flattened subtree
        if left_end:
            left_end.right = right_subtree
        else:
            # If no left subtree was flattened, set right_end to node (current root)
            right_end = node
        
        return right_end
    
    # Start flattening the tree from the root
    flattenSubtree(root)

# Helper function to perform pre-order traversal and collect values
def preorderTraversal(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return result

# Example usage:
# Construct the example tree [1,2,5,3,4,null,6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

print("Original tree (pre-order traversal):", preorderTraversal(root))

flatten(root)

print("Flattened tree (pre-order traversal):", preorderTraversal(root))
