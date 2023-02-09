# Meta Careers 2023
# Difficulty: level 1
# ruintime limit: 5 sec

from typing import List
from queue import Queue
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  q = []  # create queue from array
  eaten = 0  # create coujnter
  
  for sushi in D:
    # Check already eaten
    if sushi in q:
      print("no opp")
    else:
      eaten+=1
      # Cache what is eaten
      if len(q) < K:
        # fill queue put()
        q.append(sushi)
      else:
        # pop out First-Out
        rm = q.pop(0)
        # append Next-In
        q.append(sushi)
  
  return eaten
