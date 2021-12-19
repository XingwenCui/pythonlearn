def sum(a):
	total = 0
	for i in range(len(a)):
		total += a[i]
	return total


if __name__ == '__main__':
    a = 1
    b = 2
    c = [1,2,3,4,5]
    d = sum(c)
    print(d)
