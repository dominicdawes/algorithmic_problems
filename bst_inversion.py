# helper functions
def binaryTree():
  # insert constructor here

# code solution here
def invertTree(root):
	if root:
		temp = root.left
		root.right = temp   # swap R
		root.left = root.right   # swap L
		
		invertTree(root.left)
		invertTree(root.right)
    return root
	else:
		return None
  
if __name__ == "__main__":
  print("binary search tree inversion exercise")
  rt = binaryTree()
  inverted = invertTree(rt)  # double check helper functions with HackerRank
