

arr = range(16)

def decompose(arr):

	if len(arr) == 1:
		return arr

	left = decompose(arr[1::2])
	right = decompose(arr[0::2])

	return right + left 

print decompose(arr)
