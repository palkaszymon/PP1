num1=[2,3,2,5,8,1,9,8]
num2=[]
for i in num1:
    if i not in num2:
        num2.append(i)
print(num2)