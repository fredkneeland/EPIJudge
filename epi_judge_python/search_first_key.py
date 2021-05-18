from typing import List

from test_framework import generic_test


def search_first_of_k(A, k):
	if len(A) == 0:
		return -1

	if A[0] == k:
		return 0

	l, u, m = 0, len(A)-1, int((len(A)-1)/2)

	lastLowest = 0

	while l <= u:
		if A[m] == k:
			break
		if A[m] > k:
			u = m - 1
		else:
			lastLowest = m
			l = m + 1
		m = int((u-l)/2+l)

	# verify that we actually found the value
	if A[m] != k:
		return -1

	# start with setting up our variables for isolating the first occurance
	u = m
	m = int((u-l)/2+l)
	l = lastLowest

	# search binary to find the lower bound of the index number
	while A[l] != k:
		if A[m] == k:
			u = m-1
		else:
			l = m+1
		m = int((u-l)/2+l)

	return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
