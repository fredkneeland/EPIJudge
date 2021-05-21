from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
									 individual_play_scores: List[int]) -> int:

	
	# return score_calc_brute_force(final_score, individual_play_scores)
	# return score_calc(final_score, individual_play_scores)

	# this solution is waaaay faster than the other two (:
	return score_calc_with_arrays(final_score, individual_play_scores)

# build an array of all possible ways to score each one only adding unique lists and then sort the lists
def score_calc_brute_force(final_score, scores):
	# print("new: "+str(final_score))
	# okay, so I want to go from 1 to final_score and count the number of ways I can add up to that score

	counts = [[] for x in range(final_score+1)]
	for i in range(1, final_score+1):
		# print("i: " + str(i))
		for score in scores:
			# we add the first time we get to a score
			if i == score:
				# print("add first score: " + str(score))
				counts[i].append([score])

			# if we can add to an existing score then we go ahead and add that
			if i-score >= 0 and len(counts[i-score]) > 0:
				for oldScore in counts[i-score]:
					newScore = oldScore.copy()
					newScore.append(score)
					newScore.sort()
					if not newScore in counts[i]:
						counts[i].append(newScore)
						print("add score: " + str(newScore))
		print("scores: " + str(counts[i]))


	return len(counts[-1])

# recursively figure out the scores for all the children of the current-score
def score_calc(final_score, scores):
	if final_score <= 0:
		return 0

	if len(scores) == 0:
		return 0

	if len(scores) == 1:
		if final_score % scores[0] == 0:
			# print("found: " + str(scores[0]) + " count: "+str(final_score/scores[0]))
			return 1
		return 0

	count = 0
	newScores = scores.copy()
	score = newScores.pop()
	for i in range(int(final_score/score)+1):
		left_over = final_score-i*score

		if left_over == 0:
			count += 1
		else:
			count += score_calc(final_score-i*score, newScores)

	return count

# use a 2d array to save previous scores and build a solution
def score_calc_with_arrays(final_score, scores):
	if final_score == 0:
		return 1

	# build a 2 dimensional array
	previous_scores = [[0 for y in range(len(scores))] for x in range(0, final_score)]

	for i in range(1, final_score+1):
		for j in range(len(scores)):
			score = scores[j]
			if i == score:
				previous_scores[i-1][j] = 1
			elif i > score:
				for k in range(j+1):
					previous_scores[i-1][j] += previous_scores[i-score-1][k]

	# print("-------")
	# print(str(previous_scores))
	total_score = 0
	for i in range(len(scores)):
		total_score += previous_scores[-1][i]

	return total_score

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('number_of_score_combinations.py',
									   'number_of_score_combinations.tsv',
									   num_combinations_for_final_score))
