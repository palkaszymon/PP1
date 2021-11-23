with open("big.txt") as f:
    while f.readline():
        for i in range(0,5):
            line=f.readline()             
            if line:
                print(line)
            else:
                break
        keypress = input("Press Enter for the next five lines")
        if keypress !="":
            break