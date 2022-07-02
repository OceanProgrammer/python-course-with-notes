from functools import reduce


def multiply(n):
    return n*3

l = [3,6,9]

func_list = list(map(multiply, l))
print(func_list)

def _filter_(i):
    if len(i)>2:
        return True
    else:
        return False

l2 = ["ok", "good", "i", "", "happy"]
filter_iter = list(filter(_filter_, l2))
print(filter_iter)

def multiply(k, m):
    return k*m

l3 = [1,2,3,4,5]
reduce_list = reduce(multiply, l3)
print(reduce_list)