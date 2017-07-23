def cycle(limit: int) -> int:
	remainders = set()
	remainder = 1
	while remainder != 0 and not remainder in remainders:
		remainders.add(remainder)
		remainder = (remainder * 10) % limit
	return len(remainders)

if __name__ == '__main__':
	limit = 1000
	longest_cycle = max([(n, cycle(n)) for n in range(2, limit+1)], key = lambda p: p[1])
	print(longest_cycle)