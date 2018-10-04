
class MinHeap:
	def __init__(self):
		self.items = []

	def getLeftChildIndex(self, index):
		return index * 2 + 1

	def getRightChildIndex(self, index):
		return index * 2 + 2

	def getParentIndex(self, index):
		return (index - 1) // 2

	def hasLeftChild(self, index):
		return self.getLeftChildIndex(index) < len(self.items)

	def hasRightChild(self, index):
		return self.getRightChildIndex(index) < len(self.items)

	def hasParent(self, index):
		return self.getParentIndex(index) >= 0

	def getLeft(self, index):
		return self.items[self.getLeftChildIndex(index)]

	def getRight(self, index):
		return self.items[self.getRightChildIndex(index)]

	def getParent(self, index):
		return self.items[self.getParentIndex(index)]

	def swap(self, index1, index2):
		self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

	def peek(self):
		if self.items != []:
			return self.items[0]
		return None

	def poll(self):
		if self.items == []:
			return None
		if len(self.items) == 1:
			return self.items.pop()	

		removed_item = self.items[0]
		self.items[0] = self.items.pop()
		self.heapifyDown()
		return removed_item

	def add(self, data):
		self.items.append(data)
		self.heapifyUp()

	def heapifyDown(self):
		index = 0
		while self.hasLeftChild(index):
			childIndex = self.getLeftChildIndex(index)
			if self.hasRightChild(index) and self.getRight(index) < self.getLeft(index):
				childIndex = self.getRightChildIndex(index)
			if self.items[childIndex] > self.items[index]:
				break
			else:
				self.swap(childIndex, index)
				index = childIndex		
		

	def heapifyUp(self):
		index = len(self.items)-1

		while self.hasParent(index) and self.getParent(index) > self.items[index]:
			self.swap(self.getParentIndex(index), index)
			index = self.getParentIndex(index)

	def getHeap(self):
		return self.items		



		




