import random
def rand_elem(array):
    a=random.randint(0, len(array)-1)
    return array[a]
print(rand_elem([1,5,8,9,10]))
