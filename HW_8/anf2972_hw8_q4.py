from BinarySearchTreeMap import *

def find_min_abs_difference(bst):

    if bst.root == None:
        raise Exception("TREE IS EMPTY!")
    if len(bst) == 1:
        raise Exception("ONLY ONE NODE, DOES NOT WORK!")
    else:

        val = abs(bst.root.item.key - bst.root.left.item.key)

        return find_helper((bst.root, val))[1]

def find_helper(node):

    new_bst = node[0]

    new_min = node[1]

    if new_bst.left != None:

        left_val = find_helper((new_bst.left, node[1]))[1]

        new_min = min(left_val, new_min)

    if new_bst.right != None:

        right_val = find_helper((new_bst.right, node[1]))[1]

        new_min = min(right_val, new_min)

    if new_bst.parent != None and new_bst.parent.left != None and new_bst.parent.parent != None and new_bst != new_bst.parent.left:

            parent = new_bst.parent.item.key

            parent_left = new_bst.parent.left.item.key

            parent_parent = new_bst.parent.parent.item.key

            new_min = min(abs(new_bst.item.key - parent), abs(new_bst.item.key - parent_parent), abs(new_bst.item.key - parent_left), new_min)

    if new_bst.parent != None and new_bst.parent.left == None and new_bst.parent.parent != None:

            parent = new_bst.parent.item.key

            parent_parent = new_bst.parent.parent.item.key

            new_min = min(abs(new_bst.item.key - parent), abs(new_bst.item.key - parent_parent), new_min)

    if new_bst.parent != None and new_bst.parent.left != None and new_bst.parent.parent == None and new_bst != new_bst.parent.left:

            parent = new_bst.parent.item.key

            parent_left = new_bst.parent.left.item.key

            new_min = min(abs(new_bst.item.key - parent), abs(new_bst.item.key - parent_left), new_min)

    if new_bst.parent != None and new_bst.parent.right != None and new_bst.parent.parent != None and new_bst != new_bst.parent.right:

            parent = new_bst.parent.item.key

            parent_right =  new_bst.parent.right.item.key

            parent_parent = new_bst.parent.parent.item.key

            new_min = min(abs(new_bst.item.key - parent), abs(new_bst.item.key - parent_parent), abs(new_bst.item.key - parent_right), new_min)

    if new_bst.parent != None and new_bst.parent.right == None and new_bst.parent.parent != None:

            parent = new_bst.parent.item.key

            parent_parent = new_bst.parent.parent.item.key

            new_min = min(abs(new_bst.item.key - parent), abs(new_bst.item.key - parent_parent), new_min)

    if new_bst.parent != None and new_bst.parent.right != None and new_bst.parent.parent == None and new_bst != new_bst.parent.right:

            parent = new_bst.parent.item.key

            parent_right =  new_bst.parent.right.item.key

            new_min = min(abs(new_bst.item.key - parent), abs(new_bst.item.key - parent_right), new_min)


    return (new_bst, new_min)

'''
bst = BinarySearchTreeMap()
bst.insert(11)
bst.insert(10)
bst.insert(20)
bst.insert(17)
bst.insert(25)
bst.insert(8)
bst.insert(4)
bst.insert(2)
bst.insert(0)
bst.insert(1)
print(find_min_abs_difference(bst))
'''