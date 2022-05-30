from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):

	prefix_exp = prefix_exp_str.split(" ")

	val = LinkedBinaryTree( update_vals ( prefix_exp , 0 )[0] )

	return val

def update_vals(pre, first_val):

		if( first_val == len (pre) -1):

			upd = int(pre[first_val])

			return ( LinkedBinaryTree.Node (upd), 1)

		else:
			x =  pre[first_val]

			if x != "+" and x != "-" and x != "/" and x!= "*":

				upd = int(pre[first_val])

				new_val = first_val + 1

				return ((LinkedBinaryTree.Node(upd), new_val))

			else:

				updates = pre[first_val]

				root_val = LinkedBinaryTree.Node(updates)

				new_val = first_val + 1

				left = update_vals(pre, new_val)

				root_val.left = left[0]

				right = update_vals(pre, left[1])

				root_val.right = right[0]

				return (root_val, right[1])


def prefix_to_postfix(prefix_exp_str):

	first_tree = create_expression_tree(prefix_exp_str)

	return " ".join(str (node_val.data) for node_val in first_tree.postorder())


