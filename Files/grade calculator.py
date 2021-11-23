import re
with open("grades.txt") as f:
    text=f.read()
gradelist=re.findall("\d[.]\d",text)
sum=0
for grade in gradelist:
    sum+=float(grade)
average=sum/len(gradelist)
print(average)