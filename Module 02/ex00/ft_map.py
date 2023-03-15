def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	try:
		return [function_to_apply(x) for x in iterable]
	except:
		return None
	
#TEST
x = [1, 2, 3, 4, 5]
print(list(ft_map(lambda t: t + 1, x)))
print(list(map(lambda t: t + 1, x)))