from bubblesort import bubblesort
result=[]
def minmax(array):
    bubblesort(array)
    result.append(array[0])
    result.append(array[-1])
    return result
print(minmax([4,2,8,4,7,9,5]))
