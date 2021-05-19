from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
	if tree == None:
		return True
	
	a, b, is_binary_tree = get_smallest_and_biggest(tree)
	return is_binary_tree

# okay, I want to return the greatest and smallest value of my children
def get_smallest_and_biggest(tree: BinaryTreeNode): # -> int, int, bool:
	if tree.left == None and tree.right == None:
		return tree.data, tree.data, True

	smallest = tree.data
	biggest = tree.data

	if tree.left != None:
		smallest, lChildBiggest, valid = get_smallest_and_biggest(tree.left)
		if not valid or lChildBiggest > tree.data:
			return -1, -1, False

	if tree.right != None:
		rChildSmallest, biggest, valid = get_smallest_and_biggest(tree.right)

		if not valid or rChildSmallest < tree.data:
			return -1, -1, False

	return smallest, biggest, True 

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
									   is_binary_tree_bst))
