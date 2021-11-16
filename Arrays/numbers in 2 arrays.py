num1=[4,36,12,28,9,44,5]
num2=[5,1,36]
num3=[]
for i in num1:
    if i not in num2:
        num3.append(i)
print(num3)