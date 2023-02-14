# Level 2 Difficulty

from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  frogs = sorted(P)
  first_frog = frogs[0]
  last_frog = frogs[F-1] 
  
  # Verbose formula: F + (N - F - 1) - (min(P) - 1)
  # Simplified formula: N - min(P)

  # hopping over any other frogs on intermediate lily pads along the way
  return N - min(P)

#   This also works however I need to review why
#   minimum = N
  
#   for i in range(0, F):
#     if P[i] < minimum:
#       minimum = P[i]

#   return N - minimum
