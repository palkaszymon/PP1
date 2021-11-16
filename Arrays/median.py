from bubblesort import bubblesort
def median(array):
    bubblesort(array)
    if len(array)%2!=0:
        return array[int(len(array)/2+int(len(array)%2))-1]
    else:
        a=len(array)/2
        return (array[int(a)-1]+array[int(a)])/2
print(median([1,0,9,4,6]))
