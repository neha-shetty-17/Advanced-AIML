import math
from itertools import permutations

# Number of distinct balls in the urn (3 balls: R, B, G)
total_balls = 3
balls = ['R', 'B', 'G']

# Total possible outcomes: ways to arrange 2 balls from 3 distinct balls
total_outcomes = math.perm(total_balls, 2)

# Define events:
event_red_first = [('R', 'B'), ('R', 'G')]  # Red comes first
event_blue_first = [('B', 'R'), ('B', 'G')]  # Blue comes first
event_green_first = [('G', 'R'), ('G', 'B')]  # Green comes first

# Calculate favorable outcomes for each event
favorable_red_first = len(event_red_first)
favorable_blue_first = len(event_blue_first)
favorable_green_first = len(event_green_first)

# Calculate probabilities for each event
probability_red_first = favorable_red_first / total_outcomes
probability_blue_first = favorable_blue_first / total_outcomes
probability_green_first = favorable_green_first / total_outcomes

# Output results
print(f"Total number of outcomes (ways to arrange 2 balls from 3): {total_outcomes}")
print("\nEvent Definitions:")
print("Event 1: Red first ->", event_red_first)
print("Event 2: Blue first ->", event_blue_first)
print("Event 3: Green first ->", event_green_first)

print("\nProbabilities of Events:")
print(f"Probability of Red first (event 1): {probability_red_first:.4f}")
print(f"Probability of Blue first (event 2): {probability_blue_first:.4f}")
print(f"Probability of Green first (event 3): {probability_green_first:.4f}")

# Generating all possible outcomes (permutations of 2 balls from 3)
all_permutations = list(permutations(balls, 2))
print("\nAll Possible Outcomes (2-ball permutations):")
print(*all_permutations, sep="\n")

# Now, let's add a calculation for any other event like a specific sequence (e.g., 'R' then 'G')
specific_event = [('R', 'G')]  # Sequence of Red first and Green second
favorable_specific_event = len(specific_event)
probability_specific_event = favorable_specific_event / total_outcomes

print(f"\nProbability of drawing Red first and Green second: {probability_specific_event:.4f}")
