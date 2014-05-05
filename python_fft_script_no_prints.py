import math
import numpy as np
import matplotlib.pyplot as plt

pi = 3.14159
e = 2.7182818284


"""Takes a time domain waveform, reorganizes it as a whole bunch of smaller arrays of one point each, so that converting to the
frequency domain can be done in constant time."""
def decompose(arr):

	if len(arr) == 1:
		return arr

	left = decompose(arr[1::2])
	right = decompose(arr[0::2])

	return right + left 

"""Takes an array of frequencies (which are the same as the time domain points!) right after they have been decomposed, and 
recomposes them one level at a time."""
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
	
	# calculating some of the constants for this level
	samples_in_level = 2**(current_level + 1) # level is one higher, since we start by combining 2 points, and math indexes from 1
	total_data_points = len(arr)
	num_separate_arrays = total_data_points/samples_in_level	

	return_combined_array = []
	for sub_array_number in range(num_separate_arrays):
		# we need to pull one sub array out of the larger full array
		starting_index = sub_array_number*samples_in_level
		middle_index = starting_index + (samples_in_level/2)
		ending_index = starting_index + samples_in_level
		
		# now, separate this sub array into even and odd, in preparation for the butterfly
		even_components = [arr[i] for i in range(starting_index, middle_index)]
		odd_components = [arr[i] for i in range(middle_index, ending_index)]
				
		# now, do the butterfly with the even and odd array
		full_combined_array = butterfly(even_components, odd_components)
		return_combined_array += full_combined_array	
		
	return return_combined_array

"""This function takes in an even and an odd array and preforms the butterfly on them, returning the appropriately combined array."""
def butterfly(even_array, odd_array):
	
	combined_array_neg = [] # these will hold the pos and neg arrays after the butterfly has been computed
	combined_array_pos = []
	num_total_samples = 2 * len(odd_array) # length of even + length of odd, but they are the same length
	for sample in range(len(odd_array)):
		# calculate the all-magic twiddle factor. see notes for more on how this is calculated, or why it makes sense, if you care.
		twiddle_factor = calculate_twiddle_factor(num_total_samples, sample)
		
		# calculate the appropriate samples based on the butterfly like shape of the FFT recomposition
		negative_sample = (-1 *odd_array[sample] * twiddle_factor) + even_array[sample]
		positive_sample = odd_array[sample] * twiddle_factor + even_array[sample]
		combined_array_neg.append(negative_sample)
		combined_array_pos.append(positive_sample)
	# after both the pos and neg arrays have had the full butterfly preformed on them, they can be recombined to complete the butterfly step.
	completed_array = combined_array_pos + combined_array_neg
	return completed_array

"""Based on the two parameters that change as the butterfly is computed (the number of samples in the given level, and the sample number
being worked on), this function calculates the appropriate twiddle factor."""
def calculate_twiddle_factor(num_samples, sample_number):
	# UPDATE: This may not be neccissary: I believe that my program already handles this, by passing in the numbers
	# reduced to the appropriate part of the unit circle.
	#reduced_sample_number = sample_number%(num_samples/2) # due to the symitry of the FFT, the samples only need to go 
	# halfway around the unit circle. Since the unit circle is split up into X increments, where X is the number of samples in
	# the current level, we can mod divide by num_samples/2 to bring the sample number into the correct half of the unit circle.
	
	angle = -sample_number/(num_samples*1.0) # convert to float
	# note that convention has the angles work their way around the unit circle clockwise from 0 degrees, resulting in negative angles.
	# aslo, current units are percent of the unit circle (pretty non standard.)
	
	angle = angle * 2 * pi # convert angle to radians
	
	# now, we actually calculate the twiddle factor based of the unit cirle (for the complex plane)
	real_part = math.cos(angle)
	imaginary_part = math.sin(angle)
	twiddle_factor = real_part + 1j*imaginary_part

	return twiddle_factor

def full_FFT(input_waveform):
	decomposed_array = decompose(input_waveform)
	recomposed_frequency = recompose_all_levels(decomposed_array)
	return recomposed_frequency

	
"""Tests the FFT functions, and displays a visual of the frequency content of various waves."""
def main():
	original_timeseries = range(16)
	
	""" 
	# sine wave
	time_points = np.linspace(0,10,64)
	original_timeseries = []
	for time_point in time_points:
		original_timeseries.append(math.cos(time_point))
	"""
		
	print("Original Timeseries Points: " + str(original_timeseries))
	print("Number of original points: " + str(len(original_timeseries)))
	decomposed_array = decompose(original_timeseries)
	print("Decomposed Array: " + str(decomposed_array))
	
	print("")
	recomposed_frequency = recompose_all_levels(decomposed_array)
	print("Fully recomposed frequency content: " + str(recomposed_frequency))
	
	#plt.plot(time_points, original_timeseries)
	#plt.show()

	
if __name__ == '__main__':
	main()

