from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
	newArray = []

	i, j = 0, 0

	while i < len(A) and j < len(B):
		if A[i] == B[j]:
			if len(newArray) == 0 or newArray[len(newArray)-1] != A[i]:
				newArray.append(A[i])
			i += 1
			j += 1
		elif A[i] > B[j]:
			j += 1
		else:
			i += 1

	return newArray

# if we had a really large array and a really short array then we would want to do a binary search for each element in the small array in the large array to see if it was in there or not?



if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('intersect_sorted_arrays.py',
									   'intersect_sorted_arrays.tsv',
									   intersect_two_sorted_arrays))
