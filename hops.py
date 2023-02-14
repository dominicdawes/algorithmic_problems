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
