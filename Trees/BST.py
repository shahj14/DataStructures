class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def insert(self, data):
		new_node = Node(data)
		if self.root is None:
			self.root = new_node
		else:
			curr = self.root
			while curr:
				if curr.data > data:
					#go left
					if curr.left is None:
						curr.left = new_node
						break
					else:	
						curr = curr.left
				else:
					#go right
					if curr.right is None:
						curr.right = new_node
						break
					else:	
						 curr = curr.right
			

	def exists(self, data):
		if self.root is None:
			return False
		else:
			curr = self.root
			while curr:
				if curr.data == data:
					return True
				elif curr.data > data:
					curr = curr.left
				else:
					curr = curr.right
			return False

	def getMin(self):
		if self.root is None:
			return None
		else:
			curr = self.root
			while curr.left:
				curr = curr.left
			return curr.data	

	def getMax(self):
		if self.root is None:
			return None
		else:
			curr = self.root
			while curr.right:
				curr = curr.right
			return curr.data		
			
	def printInorder(self, curr):
		if curr.left:
			self.printInorder(curr.left)
		print(curr.data)
		if curr.right:
			self.printInorder(curr.right)								

	def empty(self):
		return self.root is None

	def getRoot(self):
		return self.root

	def depth(self, root):
	    if root is None:
	        return 0
	    
	    leftCount = height(root.left)
	    rightCount = height(root.right)
	    
	    if leftCount > rightCount:
	        return leftCount + 1
	    return rightCount + 1										