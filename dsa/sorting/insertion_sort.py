

def insertSort(array):
	array_len = len(array)
	for i in range(1,array_len):
		ele = array[i]
		hole = i

		while (hole>0 and array[hole-1]>ele):
			array[hole] = array[hole-1]
			hole = hole - 1
		array[hole] = ele
		print(array)

	return array

insertSort([7,2,4,1,5,3,0])
