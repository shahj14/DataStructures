
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None	

	def addFirst(self, data):
		node = Node(data, self.head)
		self.head = node
		return self.head

	def deleteFirst(self):
		if self.head:
			self.head = self.head.next
		return self.head	

	def addLast(self, data):
		node = self.head
		if node is None:
			self.head = Node(data)
			return self.head

		while node and node.next:
			node = node.next

		node.next = Node(data)
		return self.head	

	def deleteLast(self):
		if self.head:
			node = self.head
			while node.next.next:
				node = node.next

			node.next = None
		return self.head	

	def printList(self):
		node = self.head
		while node:
			print(node.data)
			node = node.next

	def empty(self):
		return self.head == None		