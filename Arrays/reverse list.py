numbers=[15,8,31,47,2,19]
numbers2=[]
x=len(numbers)-1
for i in range(x,-1,-1):
    numbers2.append(numbers[i])
print(f"""Normal order: {numbers}, 
Reversed order: {numbers2}""")