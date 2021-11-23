with open("big.txt") as f, open("copy.txt", "w") as copy:
    file=f.read()
    copy.write(file)