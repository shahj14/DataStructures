
def binary_search(arr, search):
	new_arr = sorted(arr)

	high = len(new_arr) -1
	low = 0

	while (low <= high):
		mid = (low + high) // 2

		item = new_arr[mid]

		if item == search:
			return True
		elif item < search:
			low = mid + 1
		else:
			high = mid - 1
	return False		


def binary_search_closest(arr, search):
	new_arr = sorted(arr)	

	high = len(new_arr) -1
	low = 0

	while (low < high):
		mid = (low + high) // 2

		if new_arr[mid] == search:
			return new_arr[mid]
		elif high - low == 1:		
			if abs(new_arr[low] - search) < abs(new_arr[high] - search):
				return new_arr[low]
			else:
				return new_arr[high]		
		elif new_arr[mid] < search:
			low = mid
		else:
			high = mid		