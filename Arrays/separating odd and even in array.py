array=[6,8,3,1,0,5,7]
odd=[]
even=[]
result=[]
for i in array:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
result.extend(even)
result.extend(odd)
print(result)
