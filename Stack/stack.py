
class Stack:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.append(item)

	def pop(self):
		if self.list != []:
			return self.list.pop()
		return None	

	def peek(self):
		if self.list != []:
			return self.list[-1]
		return None	

	def size(self):
		return len(self.list)

	def empty(self):
		return self.size() == 0
