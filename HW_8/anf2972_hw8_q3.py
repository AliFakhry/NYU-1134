from BinarySearchTreeMap import *

def restore_bst(prefix_lst):

    BST = BinarySearchTreeMap()

    if len(prefix_lst) == 0:
        return BST

    else:
        min_val = min(prefix_lst)
        max_val = max(prefix_lst)
        root_val = restore_helper(prefix_lst, 0, min_val-1, max_val+1)[0]
        BST.root = root_val
        return BST

def restore_helper(prefix_lst, index_val, min_val, max_val):

    if index_val > len(prefix_lst)-1:

        return (None, index_val)

    else:

        print("MIN_VAL", min_val)
        print("MAX_VAL", max_val)

        new_ind = prefix_lst[index_val]

        if new_ind > max_val:
            print("MAX",new_ind)
            return (None, index_val)

        if new_ind < min_val:
            print("MIN",new_ind)
            return (None, index_val)

        item = BinarySearchTreeMap.Item(new_ind)
        root = BinarySearchTreeMap.Node(item)

        index_val += 1

        left_it =  restore_helper(prefix_lst, index_val, min_val, new_ind - 1)

        root.left =  left_it[0]
        index_val =  left_it[1]

        right_it =  restore_helper(prefix_lst, index_val, new_ind + 1, max_val)

        root.right =  right_it[0]
        index_val =   right_it[1]

        return (root, index_val)

# val = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
#
# for x in val:
#     print(x)