from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
	if L1 == None:
		return L2
	elif L2 == None:
		return L1

	temp1 = L1
	temp2 = L2
	current = None

	if L1.data < L2.data:
		current = temp1
		temp1 = temp1.next
	else:
		current = temp2
		temp2 = temp2.next

	start = current

	while temp1 != None and temp2 != None:
		if temp1.data < temp2.data:
			current.next, temp1 = temp1, temp1.next
		else:
			current.next, temp2 = temp2, temp2.next
		current = current.next

	if temp1 != None:
		current.next = temp1
	elif temp2 != None:
		current.next = temp2
	
	return start


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
