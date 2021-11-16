# def lettercount(n):
#     return str(n).count("a")
# print(lettercount("You never get a second chance to make a first impression"))
def lettercount2(string, char):
    count=0
    for letter in str(string):
        if letter==char:
            count+=1
    return count
print(lettercount2("You never get a second chance to make a first impression", "a"))
