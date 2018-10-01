
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

	def deleteFirst(self):
		if self.head:
			delete_node = self.head
			self.head = self.head.next
			return delete_node.data
		return None	

	def addLast(self, data):
		node = self.head
		if node is None:
			self.head = Node(data)

		while node and node.next:
			node = node.next

		node.next = Node(data)

	def deleteLast(self):
		if self.size() == 1:
			delete_node = self.head
			self.head = None
			return delete_node.data
		if self.head:
			node = self.head
			while node.next.next:
				node = node.next

			delete_node = node.next
			node.next = None
			return delete_node.data
		return None		

	def printList(self):
		node = self.head
		while node:
			print(node.data)
			node = node.next

	def empty(self):
		return self.head == None

	def size(self):
		count = 0
		node = self.head
		while node:
			count += 1
			node = node.next
		return count				