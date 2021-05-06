def count_k(n,k):
	if (n == 0) or (n == 1):
		return 1
	elif n < 0:
		return 0
	count = 0
	for i in range(1,k+1):
		count += count_k(n-i,k)
	return count


def even_weighted(s):
	return [i*s[i] for i in range(len(s)) if i%2==0]


def max_product(s):
	if(len(s) == 0):
		return 1
	if (len(s) == 1) or (len(s) == 2):
		return max(s)
	else:
		return max(s[0]*max_product(s[2:]),s[1]*max_product(s[3:]))


def check_hole_number(n):
	
	if len(str(n)) == 3:
		digits = [int(x) for x in list(str(n))]
		return (digits[0]>digits[1]) and (digits[2]>digits[1])
	else:
		return check_hole_number(int(str(n)[:3])) and check_hole_number(int(str(n)[2:]))


def check_incr(n):
	digits = [int(x) for x in list(str(n))]
	if_incr = True
	for i in range(len(digits)-1):
		if_incr = if_incr and (digits[i]<digits[i+1])
	return if_incr


def check_decr(n):
	digits = [x for x in list(str(n))]
	digits.reverse()
	num = int(''.join(digits)) 
	return check_incr(num)


def check_mountain_number(n):
	if check_incr(n):
		return True
	elif check_decr(n):
		return True
	else:
		digits = [int(x) for x in list(str(n))]
		maximum_index = digits.index(max(digits))
		return check_incr(int(str(n)[:maximum_index])) and check_decr(int(str(n)[maximum_index:]))


def merge(s1,s2):
	i = 0
	j = 0
	result = []
	while (i < len(s1)) and (j < len(s2)):
		if s1[i] <= s2[j]:
			result.append(s1[i])
			i += 1
		else:
			result.append(s2[j])
			j += 1
	while i < len(s1):
		result.append(s1[i])
		i += 1
	while j < len(s2):
		result.append(s2[j])
		j += 1
	return result


def mario_number(level):
	if len(level) <= 2:
		return 1
	else:
		ways = 0
		if level[1] != 'P':
			ways += mario_number(level[1:])
		if level[2] != 'P':
			ways += mario_number(level[2:])
	return ways









