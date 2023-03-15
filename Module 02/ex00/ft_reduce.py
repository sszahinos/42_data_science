from functools import reduce

def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	result = iterable[0]
	count = -1
	for x in iterable:
		count += 1
		if count == 0:
			continue
		result = function_to_apply(result, x)
	return result

#TEST
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, lst))