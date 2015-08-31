class Node:
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

	def insert(self,data):
		if self.key:
			if data < self.key:
				if self.left:
					self.left.insert(data)
				else:
					self.left = Node(data)
			else:
				if self.right:
					self.right.insert(data)
				else:
					self.right = Node(data)
		else:
			self.key = Node(data)
	def display(self):
		if self.key:
			print self.key
			if self.left:
				self.left.display()
			if self.right:
				self.right.display()

def chkHeight(node):
	if node == None:
		return 0
	else:
		leftheight = chkHeight(node.left)
		if leftheight == -1:
			return -1
		rightheight = chkHeight(node.right)
		if rightheight == -1:
			return -1
		heightdiff =  leftheight - rightheight 
		if abs(heightdiff) > 1:
			return -1
		else:
			return max(leftheight,rightheight) + 1
def isbalanced(node):
	if chkHeight(node) == -1:
		return False
	else:
		return True


nodes = Node(10)
nodes.insert(12)
nodes.insert(8)
nodes.insert(6)
nodes.insert(14)
nodes.insert(1)
nodes.display()
print isbalanced(nodes)