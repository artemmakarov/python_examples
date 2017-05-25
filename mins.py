def min1(*args):
	res = args[0]
	for arg in args[1:]:
		if arg < res:
			res = arg
	return res

def min2(first, *rest):
	for arg in rest:
		if arg < rest:
			first = arg
	return first

print(min1(23,4,5,6,2,4,66,1,5,))
print(min2('aa','bb','cc','dd')) # err! < not supported str and tuple!