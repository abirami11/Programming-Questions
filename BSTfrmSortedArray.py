
class TreeNode:
	def __init__(self, key, left=None,right=None,parent = None):
		self.leftChild = left
		self.rightChild = right
		self.keyValue = key
	def display_tree(self):
		if self.keyValue:
			print self.keyValue
			if self.leftChild:
				self.leftChild.display_tree()
			if self.rightChild:
				self.rightChild.display_tree()
		else:
			return None

def bstfromSortedArray(A, start, end):
	if end < start:
		#print end,"less than",start
		return None
	mid = (start + end)//2
	#print mid ,"Value is", A[mid]
	#print start,end
	node = TreeNode(A[mid])
	# print A[mid]
	node.leftChild = bstfromSortedArray(A, start, mid - 1)
	node.rightChild = bstfromSortedArray(A, mid + 1, end)
	return node


A= [2,4,6,8,10,12]
node = bstfromSortedArray(A,0,len(A)-1)
node.display_tree()
