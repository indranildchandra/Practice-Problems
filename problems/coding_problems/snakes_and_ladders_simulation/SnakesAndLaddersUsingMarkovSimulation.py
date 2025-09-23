# Snakes and Ladders game simulation, roll a dice - go from 0 to 100
# Use Markov Simulation
# Snakes and Ladders - Test Scenario
# Probability of faces -> 0.32,0.32,0.12,0.04,0.07,0.13
# Ladders -> 32,62 42,68 12,98
# Snakes -> 95,13 97,25 93,37 79,27 75,19 49,47 67,17

import random
import numpy as np

def get_dice_value(face_prob_arr):
	## Approach 1 -> Complex, but consumes less time.
	# random_val = random.random() # random.randint(1, 6)
	# # print(random_val)
	# face_prob_sum_arr = list()
	# curr_sum = face_prob_arr[0]
	# for counter, face_prob in enumerate(face_prob_arr):
	# 	if counter == 0:
	# 		face_prob_sum_arr.append(curr_sum)
	# 	else:
	# 		curr_sum += face_prob_arr[counter]
	# 		face_prob_sum_arr.append(curr_sum)
	# if random_val>=0 and random_val<=face_prob_sum_arr[0]:
	# 	dice_value = 1
	# elif random_val>face_prob_sum_arr[0] and random_val<=face_prob_sum_arr[1]:
	# 	dice_value = 2
	# elif random_val>face_prob_sum_arr[1] and random_val<=face_prob_sum_arr[2]:
	# 	dice_value = 3
	# elif random_val>face_prob_sum_arr[2] and random_val<=face_prob_sum_arr[3]:
	# 	dice_value = 4
	# elif random_val>face_prob_sum_arr[3] and random_val<=face_prob_sum_arr[4]:
	# 	dice_value = 5
	# elif random_val>face_prob_sum_arr[4] and random_val<=face_prob_sum_arr[5]:
	# 	dice_value = 6
	# else:
	# 	dice_value = None

	## Approach 2 -> Simple, but consumes more time and uses external dependency numpy.
	dice_value = np.random.choice(a=[1,2,3,4,5,6], p=face_prob_arr, size=1, replace=False)[0]
	# For running the simulation 2000 times, approach 2 consumes approximately 33x more time as compared to approach 1.

	## Approach 3 -> Simple, but requires client to run Python 3.6 or higher. While taking the test I was using a client with Python 3.5.2 installed in it so did not use this.
	# dice_value = random.choices(population=[1,2,3,4,5,6], weights=[0.32,0.32,0.12,0.04,0.07,0.13], k=1)[0]

	# print(dice_value)
	return dice_value


def check_if_ladder_snake(curr_pos, ladders_arr, snakes_arr):
	updated_pos = curr_pos
	for ladder in ladders_arr:
		if curr_pos == ladder[0]:
			updated_pos = ladder[1]
	if updated_pos == curr_pos:
		for snake in snakes_arr:
			if curr_pos == snake[0]:
				updated_pos = snake[1]
	return updated_pos


def run_simulation(face_prob_arr, ladders_arr, snakes_arr):
	iteration_count = 0
	curr_pos = 0
	while curr_pos < 100:
		dice_value = get_dice_value(face_prob_arr)
		curr_pos += dice_value
		curr_pos = check_if_ladder_snake(curr_pos, ladders_arr, snakes_arr)
		iteration_count += 1
	return iteration_count


## Test Case 1:
# face_prob_arr = [0.32,0.32,0.12,0.04,0.07,0.13]
# ladders_arr = [(32,62), (42,68), (12,98)]
# snakes_arr = [(95,13), (97,25), (93,37), (79,27), (75,19), (49,47), (67,17)]
# no_of_simulation_runs = 200

## Test Case 2:
face_prob_arr = [0.39,0.05,0.14,0.05,0.12,0.25]
ladders_arr = [(32,62), (44,66), (22,58), (34,60), (2,90)]
snakes_arr = [(85,7), (63,31), (87,13), (75,11), (89,33), (57,5), (71,15), (55,25)]
no_of_simulation_runs = 2000

avg_val = 0
for i in range(0, no_of_simulation_runs):
	val = run_simulation(face_prob_arr, ladders_arr, snakes_arr)
	print("For simulation run: {}, number of iterations required: {}".format(i+1, val))
	avg_val += val
print("----------------------------------------------------------------------------")
print("Average number of iterations required across all {} simulation runs: {}".format(no_of_simulation_runs, avg_val // no_of_simulation_runs))
