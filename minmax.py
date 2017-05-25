def minmax(test, *args):
	res = args[0]
	for arg in args[1:]:
		if test(arg, res):
			res = arg
	return res
	
def lessthan(x, y): return x < y   # см. lamda
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4,2,1,5,6,8,3))			
print(minmax(grtrthan, 4,2,1,5,6,8,3))