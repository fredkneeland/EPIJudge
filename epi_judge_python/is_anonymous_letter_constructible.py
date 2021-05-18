from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
	# Construct a hash map with a length 26
	counts = [0 for x in range(26)]

	# Add every letter from letter_text into the
	for l in magazine_text.lower():
		counts[ord(l)%26] += 1

	for l in letter_text.lower():
		idx = ord(l)%26
		counts[idx] -= 1

		if counts[idx] < 0:
			return False
	return True


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			'is_anonymous_letter_constructible.py',
			'is_anonymous_letter_constructible.tsv',
			is_letter_constructible_from_magazine))
