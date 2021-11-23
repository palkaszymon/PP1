with open("big.txt") as f, open("copylines.txt", "w") as copy:
    for line in f.readlines():
        copy.write(line)
