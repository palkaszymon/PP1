for a in range(1,31):
    if a%5==0 and a%3==0:
        print("BINGO")
    elif a%3==0:
        print("three")
    elif a%5==0:
        print("five")
    else:
        print(a)
        