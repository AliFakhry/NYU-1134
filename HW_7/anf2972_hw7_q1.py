from LinkedBinaryTree import *

def min_and_max(bin_tree):
    if bin_tree.root == None:
        raise Exception("Empty Tree!")
    else:
        tup = subtree_min_and_max(bin_tree.root)
        return tup

def subtree_min_and_max(root):
    min_val = root.data
    max_val = root.data
    if root.left != None and root.right != None:
        left_val = subtree_min_and_max(root.left)
        right_val = subtree_min_and_max(root.right)
        return ((min(left_val[0], right_val[0], min_val), max(left_val[1], max_val)))
    elif root.left == None and root.right != None:
        right_val = subtree_min_and_max(root.right)
        return (min(right_val[0], min_val), max(right_val[1], max_val))
    elif root.left != None and root.right == None:
        left_val = subtree_min_and_max(root.left)
        return (min(left_val[0], min_val), max(left_val[1], max_val))
    else:
        return ((min_val, max_val))



