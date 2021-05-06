def memory(n):
	def update(f):
		nonlocal n
		n = f(n)
		return n
	return update


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)



def is_min_heap(t):
	if is_leaf(t):
		return True
	else:
		ans = True
		for b in branches(t):
			ans = ans and is_min_heap(b)
		return (label(t)<=min([label(b) for b in branches(t)])) and ans

def largest_product_path(t):
    if is_leaf(t):
        return label(t)
    else:
        return label(t)*max([largest_product_path(b) for b in branches(t)])


def max_tree(t):
    if is_leaf(t):
        return t
    else:
        new_branches = [max_tree(b) for b in branches(t)]
        new_label = max([label(rt) for rt in new_branches])
        return tree(new_label,new_branches)


def all_paths(t):
    if is_leaf(t):
        return [[label(t)]]
    else:
        return [[label(t)]+all_paths(b)[0] for b in branches(t)]


def make_max_finder():
    all_els = []
    def max_finder(lst):
        nonlocal all_els
        all_els = all_els + lst
        return max(all_els)
    return max_finder


def generate_constant(x):
    while True:
        yield x

def black_hole(seq,trap):
    it_seq = iter(seq)
    while True:
        next_term = next(it_seq)
        if next_term == trap:
            break
        else:
            yield next_term
    while True:
        yield trap

r = list(black_hole(range(5), 7))
print(r)