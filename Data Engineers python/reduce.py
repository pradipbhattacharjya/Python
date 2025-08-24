from functools import reduce
my_list = [1,2,3,4,5]


def square(p_x,p_y):

    return p_x+p_y

result = reduce(square,my_list)
print(result)