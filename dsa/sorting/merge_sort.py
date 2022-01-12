


def merge(left, right, array):
	nL = len(left)
	nR = len(right)
	i = 0
	j = 0
	k = 0
	while (i < nL) and (j < nR):
		if left[i] < right[j]:
			array[k] = left[i]
			i += 1
		else:
			array[k] = right[j]
			j += 1
		k += 1


	while (i < nL):
		array[k] = left[i]
		i += 1
		k += 1

	while (j < nR):
		array[k] = right[j]
		j += 1
		k += 1	



def merge_sort(array, n):
	if n < 2:
		return None

	mid = n // 2

	left = array[:mid]
	right = array[mid:]

	merge_sort(left, mid)
	merge_sort(right, (n - mid))
	merge(left, right, array)

	print(array)

l = [5,6,4,3,7,2,1]
merge_sort(l, len(l))





