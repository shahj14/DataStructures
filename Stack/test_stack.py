from stack import *
from pytest import fixture

@fixture
def generate_stack():
	test_stack = Stack()
	return test_stack

def test_add_to_stack(generate_stack):
	generate_stack.push(5)
	assert generate_stack.peek() == 5

def test_pop_stack(generate_stack):
	generate_stack.push(9)
	generate_stack.push(7)
	assert generate_stack.pop() == 7
	assert generate_stack.pop() == 9
	assert generate_stack.pop() == None

def test_peek_stack(generate_stack):
	assert generate_stack.peek() == None
	generate_stack.push(4)
	generate_stack.push(6)
	assert generate_stack.peek() == 6
	generate_stack.pop()
	assert generate_stack.peek() == 4

def test_empty_stack(generate_stack):
	assert generate_stack.empty() == True
	generate_stack.push(5)
	assert generate_stack.empty() == False	

def	test_stack_length(generate_stack):
	generate_stack.push(6)
	generate_stack.push(8)
	generate_stack.pop()
	assert generate_stack.size() == 1
	generate_stack.pop()
	assert generate_stack.size() == 0
