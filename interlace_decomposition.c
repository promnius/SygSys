//gcc -Wall -g interlace_decomposition.c -o interlace_decomposition

#include <stdio.h>

#define K_LENGTH_OF_SIGNAL 8

char signal[K_LENGTH_OF_SIGNAL] = {0, 1, 2, 3, 4, 5, 6, 7,};

char odd_signals[K_LENGTH_OF_SIGNAL/2] = {};
char even_signals[K_LENGTH_OF_SIGNAL/2] = {};


void find_odd_components_of_signal(int length_of_array) {
	
	int i;
	for (i = 0; i < length_of_array; i++) {
		if( i%2 ) {
			printf("array value is odd: %d \n", signal[i]);
			odd_signals[i-1] = signal[i];
		}
	}
}


void find_even_components_of_signal(int length_of_array) {
	int i;
	for (i = 0; i < length_of_array-1; i++) {
		if( !(i%2) ) {
			printf("array value is even: %d \n", signal[i]);
			even_signals[i] = signal[i];
		}
	}
}


int main(void) {

	int length_of_array = sizeof(signal) / sizeof(signal[0]);	//note, only works for statically allocated array.
													//in practice, null-terminate signals to find end of array.

	printf("len of array is %d \n", length_of_array);

	find_odd_components_of_signal(length_of_array);
	find_even_components_of_signal(length_of_array);

	return 1;
}

