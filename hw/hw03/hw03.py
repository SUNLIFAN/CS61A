HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x < 10:
        if x == 7:
            return 1
        else:
            return 0
    else:
        if x%10 == 7:
            return 1 + num_sevens(x//10)
        else:
            return num_sevens(x//10)

def pingpong(n,k = 1,direction = 1):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    #pingpong(n,k,direction)表示最终目的地是 n, 下一站到达 k,此时的方向是 direction，离终点还需要上升的高度
    if k < n:
        if k%7 == 0 or num_sevens(k) != 0:
            return pingpong(n,k+1,-direction) + direction
        else:
            return pingpong(n,k+1,direction) + direction
    else:
        return direction
def calculate_biggest_change(total):
    k = 1
    while k <= total:
        k = k*2

    return k//2
def count_change(total,max_change = -1):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    if max_change == -1:
        my_max_change = calculate_biggest_change(total)
    else:
        my_max_change = max_change
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif my_max_change == 0:
        return 0
    else:
        return count_change(total-my_max_change,my_max_change) + count_change(total,my_max_change//2)

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n<10:
        return 0
    elif n>10 and n<100:
        if n%11 == 0:
            return 0
        else:
            return n%10 - n//10 -1
    else:
        num_str = str(n)
        first_part = int(num_str[0:2])
        last_part = int(num_str[-2:])
        mid_part = int(num_str[1:-1])
        return missing_digits(first_part) + missing_digits(last_part) + missing_digits(mid_part)

###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(start,end)
    else:
        move_stack(n-1,start,6-start-end)
        move_stack(1,start,end)
        move_stack(n-1,6-start-end,end)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda g:(lambda x:g(lambda y:x(x)(y)))(lambda x:g(lambda y:x(x)(y))))(lambda f:lambda n:1 if n == 0 else (mul(n,f(sub(n,1)))))





