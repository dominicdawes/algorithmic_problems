# 32/32 cases passed
from typing import List
# Write any import statements here
from statistics import median

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  temp_var = 1  # our starting point
  median = (len(C)+1)/2
  move_count = 0
  
  for i in range(M):
    # forward dist
    fwd_dist = abs( C[i] - temp_var )
    
    # reverse distance
    rev_dist = N - abs(C[i]-temp_var)
    
    # shortest dist gets added to the count
    if fwd_dist > rev_dist:
      print("rev", rev_dist)
      move_count+=rev_dist
    else: 
      print("fwd", fwd_dist)
      move_count+=fwd_dist
    
    temp_var = C[i]
  
  return move_count
