# def funcName(a,b,c, d):
#     print(a*b*c*d)
# funcName(3,4,5, 9)

def funcName(other, *args_):
    print(args_)
    print(other)
    product = 1
    for i in args_:
        product = product *i
    print(product)

l = [7, 3,4,5,6,7,8,9,10]
funcName(*l)

# KWARGS IS USED TO TAKE KEYWORD ARGUMENTS
def funcName(**kwargs):
    print(kwargs)

funcName(k = 5, l=6, m=7)