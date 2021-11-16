def array2string(array): 
    result=""
    for i in array:
        result+=str(i)+","
           
    return result[0:len(result)-1]
print(array2string([4,6,7,8]))
