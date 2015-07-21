# Greatest common Devisor a la Euclid's algorithm

def gcd (m, n):
	while (n != 0):
		r = m % n
		m = n
		n = r

	return m


if __name__ == '__main__':
	user = int(raw_input("Enter m (first integer): "))
	user2 = int(raw_input("Enter n (second integer): "))

	print gcd (user, user2)