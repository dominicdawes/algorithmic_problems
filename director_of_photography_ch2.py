# Solves all test cases. O(N) Sliding Window and Prefix Sum.
# https://leetcode.com/discuss/interview-question/1641064/facebook-director-of-photography-puzzle-overflow

# 1. calculate the prefixSums of P and B so you could quickly lookup the count for a given window
# 2. For every A in position i, 
#   ans += (number of Ps to the left that is within the [i-X,i-Y] window) * (number of Bs to the right that is within the [i+X,i+Y] window) 
#   ans += (number of Bs to the left that is within the [i-X,i-Y] window) * (number of Ps to the right that is within the [i+X,i+Y] window) 

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Prefix 
  prefixPSum = [0]
  prefixBSum = [0]
  
  for c in C:
    if c == "P":
      prefixPSum.append(prefixPSum[-1] + 1)
    else:
      prefixPSum.append(prefixPSum[-1])
  for c in C:
    if c == "B":
      prefixBSum.append(prefixBSum[-1] + 1)
    else:
      prefixBSum.append(prefixBSum[-1])

  result = 0
  
  def bounded(x):
    return max(0, min(x, N))
  
  for i, c in enumerate(C):
    if c == "A":
      rightWindow = (bounded(i+X), bounded(i+Y+1))
      leftWindow = (bounded(i-Y), bounded(i-X+1))
      
      leftPs = prefixPSum[leftWindow[1]] - prefixPSum[leftWindow[0]]
      rightBs = prefixBSum[rightWindow[1]] - prefixBSum[rightWindow[0]]
      result += leftPs * rightBs
      
      rightPs = prefixPSum[rightWindow[1]] - prefixPSum[rightWindow[0]]
      leftBs = prefixBSum[leftWindow[1]] - prefixBSum[leftWindow[0]]
      result += leftBs * rightPs
        
  return result
