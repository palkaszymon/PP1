array=[1,23,5,382,1,17,906]
divider="|"
for i in array:
    divider+=" "*(4-len(str(i)))+str(i)+"|"
print("-"*len(divider))
print(divider)
print("-"*len(divider))
