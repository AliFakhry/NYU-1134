from BinarySearchTreeMap import *

def create_chain_bst(n):

    new_tree = BinarySearchTreeMap()

    for i in range(1,n+1):
        new_tree.insert(i)

    return new_tree

def create_complete_bst(n):

    bst = BinarySearchTreeMap()
    add_items(bst,1,n)
    return bst

def add_items(bst, low,high):

    mid_point = (low + high)//2

    if low >= high:
        if low == high:
            bst.insert(mid_point)

    else:
        bst.insert(mid_point)
        add_items(bst,low,mid_point-1)
        add_items(bst, mid_point+1, high)


# val = create_complete_bst(8)
#
# for i in val:
#     print(i)