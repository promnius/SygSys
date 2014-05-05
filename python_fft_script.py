import math

pi = 3.14159
e = 2.7182818284



def decompose(arr):

	if len(arr) == 1:
		return arr

	left = decompose(arr[1::2])
	right = decompose(arr[0::2])

	return right + left 

def recompose_all_levels(arr):
	num_levels = math.log(len(arr),2)
	for level in range(int(num_levels)):
		arr = recompose_one_level(arr, level)
	return arr


"""Take an array of points, which is actually a number of smaller arrays combined into one, which is actually stored as a list, and
does one layer of butterfly, returning an array with half the number of smaller arrays (since every two got combined into one.)
Note that I do a lot of creating new arrays (lists) here that could be avoided, since they can just replace the existing slot in the
old list. It is easier to follow what is happening this way though."""
def recompose_one_level(arr, current_level):
	debug_local = True
	
	# twiddle factors need a function to calculate them in the future
	twiddle_factor_preloads = {}
	twiddle_factor_preloads[2] = [1]
	twiddle_factor_preloads[4] = [1, -1j]
	twiddle_factor_preloads[8] = [1,1/math.sqrt(2)-(1/math.sqrt(2))*1j,-1j, -1/math.sqrt(2) - (1/math.sqrt(2))*1j]
	print("ALL TWIDDLE FACTORS: " + str(twiddle_factor_preloads))
	
	# generating some of the variables that are used for the math.
	if debug_local: print("Attempting to recompose one level. Level number: " + str(current_level))
	samples_in_level = 2**(current_level + 1) # level is one higher, since we start by combining 2 points, and math indexes from 1
	if debug_local: print("Samples in Level: " + str(samples_in_level))
	total_data_points = len(arr)
	num_separate_arrays = total_data_points/samples_in_level
	if debug_local: print("Number of separate sub-arrays to start with: " + str(num_separate_arrays))
	
	# some algorithems try to make the math simpler by splitting the final array into two separate arrays for
	# real AND imaginary, rather than one array that uses imaginary numbers. therefore, you have to calculate the
	# twiddle factor for both the real and imaginary parts. we just use imaginary numbers.
	print("")
	
	return_combined_array = []
	combined_array = [] # This holds the list that gets returned after this level of butterflys is complete.
	# it is more computationally efficient to do in-place replacement of the existing list, but this is easier to understand.
	
	for sub_array_number in range(num_separate_arrays): # for each sub array, preform the butterfly to combine them
		if debug_local: print("recombining one sub-array. array number: " + str(sub_array_number))
		
		# extracting the two arrays (even and odd) from the original array
		starting_index = sub_array_number*samples_in_level
		middle_index = starting_index + (samples_in_level/2)
		ending_index = starting_index + samples_in_level
		even_components = [arr[i] for i in range(starting_index, middle_index)]
		odd_components = [arr[i] for i in range(middle_index, ending_index)]
		
		if debug_local: print("This sub-array is: " + str(even_components + odd_components))
		if debug_local: print("Even components: " + str(even_components))
		if debug_local: print("Odd components: " + str(odd_components))
		
		# now, do the butterfly with the even and odd array
		combined_array_neg = [] # need to label what these are.
		combined_array_pos = []
		for sample in range(len(odd_components)):
			# twiddle factors are now preloaded, based off the unit circle
			#twiddle_factor = e**(-1j*((2*pi*sample)/(len(odd_components))))
			#print("LENGTH OF ODD_COMPONENTS: " + str(len(odd_components)))
			list_of_twiddle_factors = twiddle_factor_preloads[samples_in_level]
			twiddle_factor = list_of_twiddle_factors[sample]
			
			if debug_local: print("twiddle factor for sample " + str(sample) + " is: " + str(twiddle_factor))
			combined_sample_neg = (-1 *odd_components[sample] * twiddle_factor) + even_components[sample]
			combined_sample_pos = odd_components[sample] * twiddle_factor + even_components[sample]
			combined_array_neg.append(combined_sample_neg)
			combined_array_pos.append(combined_sample_pos)
		combined_array = combined_array_pos + combined_array_neg
		if debug_local: print("recombined array for these two sub arrays: " + str(combined_array))
		return_combined_array += combined_array	
		
		print("")
	#print("return array: " + str(return_combined_array))
	return [return_combined_array]
	
def main():
	original_timeseries = range(4)
	print("Original Timeseries Points: " + str(original_timeseries))
	decomposed_array = decompose(original_timeseries)
	print("Decomposed Array: " + str(decomposed_array))
	one_level_recomposed = recompose_one_level(decomposed_array, 0)
	
	second_level_recomposed = recompose_one_level(one_level_recomposed, 1)
	
	# converting to the closest integers. fancy math required because of the imaginary parts
	#second_level_recomposed_rounded = [round(second_level_recomposed[i].real) + 1j * round(second_level_recomposed[i].imag) for i in range(len(second_level_recomposed))]
	
	third_level_recomposed = recompose_one_level(second_level_recomposed, 2)
	
	print("Original Timeseries Points (reprinted): " + str(original_timeseries))
	print("Decomposed Array (reprinted): " + str(decomposed_array))
	print("Recomposed after one level: " + str(one_level_recomposed))
	print("Recomposed after second level: " + str(second_level_recomposed))
	#print("Recomposed after second level, rounded: " + str(second_level_recomposed_rounded))
	print("Recomposed after third level: " + str(third_level_recomposed))

	
	
	print("")
	print("Now, testing the auto recomposition.")
	#auto_recomposed = recompose_all_levels(decomposed_array)
	#print("Fully recomposed frequency content: " + str(auto_recomposed))
	

def round_complex(raw):
	rounded = [round(raw[i].real) + 1j * round(raw[i].imag) for i in range(len(raw))]
	return rounded
	
	
if __name__ == '__main__':
	main()

            
"""
def recompose_one_level(arr, current_level):
    
    
    number_of_levels = math.log(arr, 2)
    
    for current_level in range(0, number_of_levels):    
    
        samples_in_level = current_level**2
    
        sinusoid_real = math.cos(pi / ((samples_in_level) / 2)  )
        sinusoid_im = math.sin(pi / ((samples_in_level) / 2)  )
        
        for sample in range(0, (samples_in_level - 1) / 2):
			pass
"""




