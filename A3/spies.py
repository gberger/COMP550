import numpy

MAX_N = 12
SHOW_M = 12

r = numpy.zeros((MAX_N+1, 20000))
r[0, 1] = 1
r[1, 1] = 1

for n in range(2, MAX_N+1):
	m = 1
	while True:
		over = 0
		for j in range(1, 20000):
			if r[n-1, j] < m:
				break
			over += 1
		r[n, m] = r[n-1, m] + over
		if r[n, m] == 0:
			break
		m += 1


print r[:MAX_N+1, 1:SHOW_M+1]
