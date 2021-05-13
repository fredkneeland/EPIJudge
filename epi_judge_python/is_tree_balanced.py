from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(node):
	bal = is_balanced(node)
	bal2, _ = node_depth2(node, 0)

	print("test1: " + str(node_depth.counter/node_depth2.counter))
	node_depth.counter = 0
	node_depth2.counter = 0
	return bal
	# return !bal2


def is_balanced(node):
	if node == None:
		return True

	if abs(node_depth(node.right)-node_depth(node.left)) > 1:
		return False
	return is_balanced(node.right) and is_balanced(node.left)

def node_depth(node):
	node_depth.counter += 1
	if node == None:
		return 0
	right_height = node_depth(node.right)
	left_height = node_depth(node.left)

	return max(right_height, left_height) + 1
node_depth.counter = 0

def node_depth2(node, height):
	node_depth2.counter += 1
	# test2 += 1
	if node == None:
		return True, height

	rBal, rMaxHeight = node_depth2(node.right, height+1)

	if not rBal:
		return False, rMaxHeight

	lBal, lMaxHeight = node_depth2(node.left, height+1)

	if not lBal:
		return False, lMaxHeight

	if abs(rMaxHeight-lMaxHeight) > 1:
		return False, max(rMaxHeight, lMaxHeight)
	return True, max(rMaxHeight, lMaxHeight)
node_depth2.counter = 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
