class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    
    # Recursively find the depth of each subtree
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    
    return 1 + max(left_height, right_height)

# Example: Tree with depth 3
#      1
#     / \
#    2   3
#       /
#      4
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
print(f"Max Depth: {max_depth(root)}") # Output: 3