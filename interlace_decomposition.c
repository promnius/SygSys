//gcc -Wall -g interlace_decomposition.c -o interlace_decomposition

#include <stdio.h>

#define K_LENGTH_OF_SIGNAL 8	//be sure to make this match the actual number of items in the signal below

char signal[K_LENGTH_OF_SIGNAL] = {0, 1, 2, 3, 4, 5, 6, 7,};




/*
char* find_odd_components_of_signal(int length_of_array) {
	char* odd_components[K_LENGTH_OF_SIGNAL/2] = {};
	int i;
	for (i = 0; i < length_of_array; i++) {
		if( i%2 ) {
			printf("array value is odd: %d \n", signal[i]);
			odd_components[i-1] = signal[i];
		}
	}
	return odd_components;
}

*/

char* find_odd_components_of_signal(char* signal_to_be_decomposed, int length_of_signal_being_decomposed) {
	char* odd_components[length_of_signal_being_decomposed] = {};	
	int i;
	for (i = 0; i < length_of_signal_being_decomposed; i++) {
		if( !(i%2) ) {
			printf("array value is odd: %d \n", char* signal_to_be_decomposed[i]);
			odd_components[i] = char* signal_to_be_decomposed[i];
		}
	}
	return odd_components;
}


char* find_even_components_of_signal(char* signal_to_be_decomposed, int length_of_signal_being_decomposed) {
	char* even_components[length_of_signal_being_decomposed] = {};	
	int i;
	for (i = 0; i < length_of_signal_being_decomposed-1; i++) {
		if( !(i%2) ) {
			printf("array value is even: %d \n", char* signal_to_be_decomposed[i]);
			even_components[i] = char* signal_to_be_decomposed[i];
		}
	}
	return even_components;
}


char* decompose(char* array, int length_of_array_being_decomposed) {
//	if (length_of_array_being_decomposed == 1) {
//		return array;
//	}
	char* left[length_of_array_being_decomposed/2] = find_even_components_of_signal(array, length_of_array_being_decomposed);
		
	return 1;	
	
}

int main(void) {

	int length_of_array = sizeof(signal) / sizeof(signal[0]);	//note, only works for statically allocated array.

	decompose(signal, length_of_array);
													//in practice, null-terminate signals to find end of array.
	printf("len of array is %d \n", length_of_array);
	

	/*

	char *odd_components = malloc(K_LENGTH_OF_SIGNAL/2);  // allocate memory from the heap
	odd_components = find_odd_components_of_signal(length_of_array);
	//find_even_components_of_signal(length_of_array);

	int length_of_odd_components = sizeof(odd_components) / sizeof(odd_components[0]);
	printf("len of odd component array is %d \n", length_of_odd_components);

	*/

	return 1;
}

