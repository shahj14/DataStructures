def insertion_sort(arr):
	new_arr = arr

	#loop from the second to the last element of array
	#skip the first element since it is already sorted 
	for i in range(1,len(new_arr)):
		#item to be inserted
		key = new_arr[i]
		#the next iteration will go backwards from the insertion element
		j = i - 1

		#iterate through sorted list while there are items
		#and the inserted item is less than the comparision element
		while j >= 0 and key < new_arr[j]:
			#shift item up in array
			new_arr[j+1] = new_arr[j]
			j -= 1
		
		#insert item at j+1 due to the subtraction from end of while loop	
		new_arr[j+1] = key

	#copy of array
	return new_arr	

def quick_sort(arr, low, high):
	#check if there is anything left to sort
	if low < high:
		#get partition index
		pi = partition(arr, low, high)

		#sort lower half
		quick_sort(arr, low, pi-1)
		#sort upper half
		quick_sort(arr, pi+1, high)

def partition(arr, low, high):
	#pivot will be top element in array
	pivot = arr[high]
	#variable to decide returned partition
	i = low - 1

	for j in range(low, high):
		if arr[j] <= pivot:
			i = i + 1
			#move item to left of pivot
			arr[i], arr[j] = arr[j], arr[i]
	#move pivot to proper position		
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def merge_sort(arr, left, right):
	if left < right:
		mid = (left + right) // 2

		merge_sort(arr, left, mid)
		merge_sort(arr, mid+1, right)

		merge(arr, left, mid, right)
	

def merge(arr, left, mid, right):
	#two arrays to merge
	#[left to mid] and [mid+1 to right]

	l1 = mid - left + 1 #length of left array
	l2 = right - mid #length of right array

	#create temporary arrays for each list half
	temp1 = [0] * l1
	temp2 = [0] * l2
	
	#copy elements to temporary arrays
	for i in range(l1):
		temp1[i] = arr[i + left]

	for j in range(l2):
		temp2[j] = arr[j + mid + 1]

	#track index of each temp list
	leftIndex = 0
	rightIndex = 0
	#track spot in the original array
	k = left

	while leftIndex < l1 and rightIndex < l2:
		if temp1[leftIndex] <= temp2[rightIndex]:
			arr[k] = temp1[leftIndex]
			leftIndex += 1
		else:
			arr[k] = temp2[rightIndex]
			rightIndex += 1
		k += 1
	
	#insert remaining values from list	
	while leftIndex < l1:
		arr[k] = temp1[leftIndex]
		leftIndex += 1
		k += 1
	while rightIndex < l2:
		arr[k] = temp2[rightIndex]
		rightIndex += 1
		k += 1


	





















	