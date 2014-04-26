use std::vec;
use std::iter;


fn generate_signal_vector(signal_length: uint) -> Vec <uint> {
		
	let vec: Vec<uint> = iter::range(0u,signal_length).collect();
	/*
	println!("{:?}", vec);
	for i in range(0, vec.len() ) {
		//println!("value is {}", vec.get(i) );
	}
	*/
	return vec;
}



fn find_odd_components_of_signal(input_signal: &[uint]) -> Vec <uint> {

//	let x: int = 0;
//	let y: uint = x as int;

//	let length: int = input_signal.len() as uint;
//	let length = input_signal.len();

	
//		println!("array value is odd: {}", i);


	let mut vec: Vec<uint> = vec!();

	for i in iter::range_step(1, input_signal.len(), 2) {
		vec.push(input_signal[i]);
	}
	
	return vec



/*
	let mut vec = Vec::new();
	for i in range(0u,16u) {
		*vec.get_mut(i) = i;		
		println!("length is {}", vec.len());
		
		println!("value is {}", vec.get(i) );
	}		
	let a = vec.get(0);
}
*/

}



fn find_even_components_of_signal(input_signal: &[uint]) -> Vec <uint> {

	let mut vec: Vec<uint> = vec!();

	for i in iter::range_step(0, input_signal.len()-1, 2) {
		vec.push(input_signal[i]);
	}
	
	return vec
	
}


fn decompose_signal(signal_to_decompose: &[uint]) -> Vec <uint> {


	if (signal_to_decompose.len() == 1) {
		return vec::Vec::from_slice(signal_to_decompose);
	}
	let mut left: Vec<uint> = decompose_signal(find_even_components_of_signal(signal_to_decompose.slice_from(0)).slice_from(0));
	let right: Vec<uint> = decompose_signal(find_odd_components_of_signal(signal_to_decompose.slice_from(0)).slice_from(0));
	left.push_all(right.slice_from(0));
	
	println!("decomposed array is {}", left);
	
	return left

}



fn main()  {
	let length:uint = 16;
	
	let signal:Vec<uint> = generate_signal_vector(length);
	find_odd_components_of_signal(signal.slice_from(0));
	find_even_components_of_signal(signal.slice_from(0));
	decompose_signal(signal.slice_from(0));
	
//	for i in iter::range_step(1, 16, 2) {
//		println!("array value is odd: {}", i);
//	}
}







/*
	let mut vec = Vec::new();
	for i in range(0u,16u) {
		*vec.get_mut(i) = i;		
		println!("length is {}", vec.len());
		
		println!("value is {}", vec.get(i) );
	}		
	let a = vec.get(0);
}
*/
