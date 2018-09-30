
class Queue:
	def __init__(self):
		self.items = []

	def empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]	

	def size(self):
		return len(self.items)	
				