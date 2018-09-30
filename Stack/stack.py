
class Stack:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.append(item)

	def pop(self):
		return self.list.pop()

	def peek(self):
		if !self.empty():
			return self.list[-1]

	def size(self):
		return len(self.list)

	def empty(self):
		return self.size() == 0
