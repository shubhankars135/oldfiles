

"""
A closure is inner function that stores and has access to the inner variables in local scope
in which it was created  
"""


def print_hello():
	msg = 'hello'

	def inner(name):
		print(msg + ' ' + name)

	return inner

new_func = print_hello()
new_func('sarika')
new_func('fill')




### decorator

"""
check if the divisor in divide function is zero through decoraator 
"""

def check_zero(func):
	def wrapper(a,b):
		if b == 0:
			print('invalid divisor')
		else:
			return func(a,b)
	return wrapper

@check_zero
def division(a,b):
	return a/b

print(division(10,0))
print(division(24,8))