



def quick_sort(array, start, end):
	if start < end:
		p_index = partition(array, start, end)
		quick_sort(array,start,p_index)
		quick_sort(array,p_index + 1,end)


def partition(array, start, end):
	print(array, start, end)
	pivot  = array[end-1]
	p_index = start

	for i in range(start, end-1):
		if (array[i] <= pivot):
			array[p_index], array[i] = array[i], array[p_index]
			p_index += 1

	array[p_index], array[end-1] = array[end-1], array[p_index]
	print(p_index)
	return p_index

l = [5,6,4,3,7,2,1]
quick_sort(l, 0, len(l))


