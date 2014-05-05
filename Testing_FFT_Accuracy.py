

import math
import python_fft_script_no_prints as fft
import numpy as np
import matplotlib.pyplot as plt

"""
old_file = open("test_data.txt", 'r', 0)
new_file = open("new_data.txt", 'w', 0)
my_input = old_file.read()
new_file.write(my_input)
"""

frequency = 10

"""Generates one of a small number of waveforms in the format used by an online calculator, so that I can take the FFT
of a multi-thousand point signal without needing to type it all in by hand. """
def generate_input_waveform(waveform_type, num_data_points):
    new_file = open("Time_Waveform.txt", 'w', 0)
    if waveform_type == "LINEAR":
        data = range(num_data_points)
    elif waveform_type == "COSINE":
        time_points = np.linspace(0,frequency,num_data_points)
        data = []
        for time_point in time_points:
            data.append(math.cos(time_point))
    elif waveform_type == "IMPULSE_MIDDLE":
        data = []
        for counter in range(num_data_points):
            if counter == round(num_data_points/2):
                data.append(1)
            else:
                data.append(0)
    output_string = ""
    for datapoint in data:
        output_string += str(datapoint)
        output_string += "\n"
    new_file.write(output_string)



"""Takes in the filename where the raw data from the online calculator is stored, and returns it as a nice list so that
it can be compared to the data from our calculator."""
def interpret_online_calculator_output(filename):
    frequency_file = open(filename, 'r', 0)
    my_input = frequency_file.read()
    is_first_number = True
    first_number = ''
    second_number = ''
    real_numbers = []
    imaginary_numbers = []
    for character in my_input:
        if character == ',':
            is_first_number = False
        elif character == 'j':
            pass
        elif character == '\n':
            is_first_number = True
            real_numbers.append(float(first_number))
            imaginary_numbers.append(float(second_number))
            first_number = ''
            second_number = ''
        else:
            if is_first_number:
                first_number+= character
            else:
                second_number+=character
    frequency_content = []
    for counter in range(len(real_numbers)):
        frequency_content.append(real_numbers[counter] + 1j * imaginary_numbers[counter])
    return frequency_content

"""Takes in two lists, one from our calculator, one from the online one, and compares them to determine if any numbers are
off by more than the acceptable amount. It then returns the maximum difference between the two. The reason for not
comparing if they are identical is that there is so many computations done on each number, that floating point rounding error
will make them have slightly different numbers 5 or 6 digits out."""
def compare_data(our_data, online_data, max_acceptable_deviation):
    is_acceptable = True
    max_deviation = 0
    if len(online_data) != len(our_data):
        print("COMPARE_DATA: Data lengths are not the same!!")
        is_acceptable = False    
    else:
        for counter in range(len(online_data)):
            real_deviation = abs((our_data[counter].real) - (online_data[counter].real))
            imaginary_deviation = abs((our_data[counter].imag) - (online_data[counter].imag))
            if real_deviation > max_acceptable_deviation or imaginary_deviation > max_acceptable_deviation:
                is_acceptable = False
            if real_deviation > max_deviation or imaginary_deviation > max_deviation:
                max_deviation = max(real_deviation, imaginary_deviation)
    return [is_acceptable, max_deviation]

def main():
    num_points = 4096
    
    # linear
    our_fft_input = range(64)
    
    """
    # sine
    time_points = np.linspace(0,frequency,num_points)
    our_fft_input = []
    for time_point in time_points:
        our_fft_input.append(math.cos(time_point))
    """
    """
    # impulse in the middle
    our_fft_input = []
    for counter in range(num_points):
        if counter == round(num_points/2):
            our_fft_input.append(1)
        else:
            our_fft_input.append(0)
    """
    
    generate_input_waveform("IMPULSE_MIDDLE",num_points)
    online_freq = interpret_online_calculator_output('Frequency_content.txt')
    our_freq = fft.full_FFT(our_fft_input)
    print("length of our frequency: " + str(len(our_freq)))
    print("length of online frequency: " + str(len(online_freq)))
    print(compare_data(our_freq,online_freq, 10E-3))
    
    
    # plot timeseries
    plt.plot(our_fft_input)
    
    # plot frequency
    plt.figure()
    our_freq_content = []
    for freq in our_freq:
        our_freq_content.append(abs(freq))
    plt.plot(our_freq_content)
    plt.show()
    
    
if __name__ == '__main__':
    main()