arr1=[1,5,3,7]
arr2=[1,43,245,3,5,67]
a=0
result=0
for i in arr1:
    if i in arr2:
        a+=1
    if a==len(arr1):
        result=True
    else:
        result=False
print(result)