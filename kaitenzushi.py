# Meta Careers 2023
# Difficulty: level 1
# ruintime limit: 5 sec

from typing import List
from queue import Queue
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here ( faster time complexity )
  Sk = set([])  # create hash set obj
  Qk = deque([]) # Doubly Ended Queue
  eaten = 0  # create counter
  
  for sushi in D:
    # Check already eaten
    if sushi not in Sk:
      if len(Sk) == K:
        sushi_old = Qk.popleft()
        Sk.remove(sushi_old) # rm old sushi from the set
      # else add to memory
      Sk.add(sushi)
      Qk.append(sushi)  # inserts at right end of the deque
      print("added")
      eaten+=1
      
#   Write your code here ( faster time complexity )     
#   q = []  # create queue from array
#   eaten = 0  # create counter
  
#   for sushi in D:
#     # Check already eaten
#     if sushi in q:
#       print("no opp")
#     else:
#       eaten+=1
#       # Cache what is eaten
#       if len(q) < K:
#         # fill queue put()
#         q.append(sushi)
#       else:
#         # pop out First-Out
#         rm = q.pop(0)
#         # append Next-In
#         q.append(sushi)
  
  return eaten
