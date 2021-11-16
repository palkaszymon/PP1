array=[1,5,7,2,9,8]
result=[]
number=int(input("Type in a number: "))
for i in array:
    if number<i:
        result.append(i)
print(result)
