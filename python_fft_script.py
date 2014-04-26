import math

pi = 3.14159

arr = range(16)

def decompose(arr):

	if len(arr) == 1:
		return arr

	left = decompose(arr[1::2])
	right = decompose(arr[0::2])

	return right + left 

print decompose(arr)

def recompose(arr, current_level):
    
    
    number_of_levels = math.log(arr, 2)
    
    for current_level in range(0, number_of_levels):    
    
        samples_in_level = current_level**2
    
        sinusoid_real = math.cos(pi / ((samples_in_level) / 2)  )
        sinusoid_im = math.sin(pi / ((samples_in_level) / 2)  )
        
        for sample in range(0, (samples_in_level - 1) / 2):





            

