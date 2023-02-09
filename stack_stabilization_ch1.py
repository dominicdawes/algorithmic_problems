from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  deflate_count = 0  # 
#    MY OLD SOLUTION (32/33 cases passed... idk what the edge case was)  
#
#    deflate_count = 0
#    for i in range(len(R)-1, 0, -1):  # iterate backwards
#      print("R_i: ", R[i])  # helper print
#      # top disk is larger than bottom disk
#      if R[i] <= R[i-1]:
#        R[i-1] = R[i]-1
#        deflate_count +=1 
#
#        if R[i-1] < 1:
#          return -1  # disk of radius zero is a failing case
#
#    # make sure at least 1 
#    if deflate_count < 1:
#      return -1

#    MY *NEW* SOLUTION 
  deflate_count = 0
  
  # the base disk radius R[N-1] needs to be g.t.e the length of the stack
  if R[N-1] >= N:
    for i in range(len(R)-2, -1, -1):
      print("R_i", R[i])
      
      # check to see that top disk is smaller than the one directly below
      if R[i] < R[i+1]:
        print("continue")

      else:
        if R[i+1] > 1:
          R[i] = R[i+1]-1
          deflate_count +=1 
        else:
          return -1
  
  else:
    return -1
  
  return deflate_count
