def square(x):
    sum_so_far = 0
    for _ in range(x):
        sum_so_far += x
	return sum_so_far  # Python3 的话运行会报语法错误，请在python2下运行

print(square(10))