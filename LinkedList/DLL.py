
class Node:
	def __init__(self, data, prev=None, next=None):
		self.data = data
		self.prev = prev
		self.next = next

class DLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def addFirst(self, data):
		node = Node(data, next=self.head)
		if self.head:
			self.head.prev = node
		if self.tail is None:
			self.tail = node

		self.size += 1	
		self.head = node
		return self.head

	def addLast(self, data):
		node = Node(data, prev=self.tail)
		if self.tail:
			self.tail.next = node
		self.tail = node

		if self.head is None:
			self.head = node

		self.size += 1
		return self.tail	


		self.head = Node(data)
		return self.head			

	def deleteFirst(self):
		if self.size == 1:
			delete_node = self.head
			self.head, self.tail = None, None
			return delete_node.data

		if self.head:
			delete_node = self.head
			self.head.next.prev = None
			self.head = self.head.next
			self.size -= 1
			return delete_node.data

		raise IndexError("List is empty, can't delete")

	def deleteLast(self):
		if self.size == 1:
			delete_node = self.head
			self.head, self.tail = None, None
			return delete_node.data

		if self.tail:
			delete_node = self.tail
			self.tail = self.tail.prev
			self.tail.next = None
			self.size -= 1
			return delete_node.data	
		
		raise IndexError("List is empty, can't delete")

	def getHead(self):
		return self.head.data

	def getTail(self):
		return self.tail.data	
	
	def empty(self):
		return self.size == 0

	def length(self):
		return self.size				

	def printList(self):
		curr = self.head
		while curr:
			print(curr.data)
			curr = curr.next
			

