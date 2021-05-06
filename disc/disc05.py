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


def height(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])


def square_tree(t):
    if is_leaf(t):
        return tree(label(t)**2)
    else:
        root = label(t)**2
        return tree(root,[square_tree(b) for b in branches(t)])


def find_path(t,x):
    if (label(t) == x) or is_leaf(t):
        return [label(t)]

    for b in branches(t):
        path = [label(t)] + find_path(b,x)
        if x in path:
            return path
    return []


"""
1.4
1. 1
2. violates the abstraction barrier,right expression should be:label(t)
3. 2
4. [2]
5. violates the abstraction barrier, the right expression should be: is_leaf(branches(t)[1])
6. [2,3]
"""


def add_this_many(x,el,lst):
    cnt_x = lst.count(x)
    for i in range(cnt_x):
        lst.append(el)


def group_by(s,fn):
    dict = {}

    for el in s:
        if fn(el) not in dict:
            dict[fn(el)] = []
        dict[fn(el)].append(el)

    return dict


def partition_options(total,biggest):

    if total <= 0:
        return [[]]
    elif biggest == 0:
        return []
    else:
        with_biggest = [option+[biggest] for option in partition_options(total-biggest,biggest) if biggest+sum(option) == total]
        without_biggest = partition_options(total,biggest-1)
        return with_biggest+without_biggest


def min_element(T,lst):
    if T == 0:
        return 0
    return min([min_element(T-el,lst) for el in lst if T >= el]) + 1






