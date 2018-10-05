

#implementations of insertion, quick, and merge sorts

def insertionSort(arr):
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

def quickSort(arr, low, high):
	#check if there is anything left to sort
	if low < high:
		#get partition index
		pi = partition(arr, low, high)

		#sort lower half
		quickSort(arr, low, pi-1)
		#sort upper half
		quickSort(arr, pi+1, high)

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