from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
	A.sort(reverse=True)
	return has_sum(A, t, 3)

def has_sum(A, t, count):
	if count == 1:
		return t in A

	for i in range(len(A)):
		if has_sum(A[i:], t-A[i], count-1):
			return True

	return False

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
									   has_three_sum))
