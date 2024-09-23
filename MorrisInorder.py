class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def morrisInorderTraversal(self, root: TreeNode):
        current = root
        result = []
        
        while current:
            if current.left is None:
                result.append(current.value)  # Visit the node
                current = current.right  # Move to the right subtree
            else:
                # Find the predecessor of the current node
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:  # Make current the right child of its predecessor
                    predecessor.right = current
                    current = current.left
                else:  # Revert the changes made to restore the original tree
                    predecessor.right = None
                    result.append(current.value)  # Visit the node
                    current = current.right  # Move to the right subtree
        
        return result
