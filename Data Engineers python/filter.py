my_list = [1,2,3,4,5]


def square(p_x):


    if(p_x % 2 == 0):
      return p_x*p_x

result = list(filter(square,my_list))
print(result)