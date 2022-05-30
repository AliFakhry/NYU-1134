
from LinkedBinaryTree import *

def is_height_balanced(bin_tree):

    if bin_tree.root == None:
        return True
    elif bin_tree.root.left == None and bin_tree.root.right == None:
        return True
    else:
        return isinstance(helper_func(bin_tree.root), tuple)

def helper_func(root):
    if root == None:
        return (True, 0)
    elif root.left == None and root.right == None:
        return (True, 1)
    else:
        left_val = helper_func(root.left)
        right_val = helper_func(root.right)
        if left_val == False or right_val == False:
            return False
        else:
            max_height = max(left_val[1], right_val[1])
            max_height += 1
            if abs(left_val[1] - right_val[1]) > 1:
                return False
            else:
                return ((True, max_height))

"""
binary_tree = LinkedBinaryTree()
root = LinkedBinaryTree.Node(3)
root.left = LinkedBinaryTree.Node(3)
root.right = LinkedBinaryTree.Node(6)
root.left.left = LinkedBinaryTree.Node(4)
root.left.right = LinkedBinaryTree.Node(1)
root.left.right.right = LinkedBinaryTree.Node(3)
binary_tree.root = root
print(is_height_balanced(binary_tree))
"""