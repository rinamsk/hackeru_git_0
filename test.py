import lesson_3_1 as ls3

def print_check_even_number(n):
	res = 'является четным числом'
	if not ls3.check_even_number(n):
		res = 'не ' + res
	print(n, res)

print_check_even_number(2)
print_check_even_number(3)
print_check_even_number(4)
print_check_even_number(10)
print_check_even_number(7)