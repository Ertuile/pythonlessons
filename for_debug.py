from for_debug2 import anotherfunc, test_func


def my_func(a,b,c):
    print('divide')
    c*=100
    anotherfunc(2)
    test_func()
    print('c=',c)
    a *= c
    return a/b

print('abc')
d=3
print(my_func(1,1,1))
m=4
l=[1,2,3,4,5]