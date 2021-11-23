with open("integer powers.txt","w") as f:
    for i in range(1,11):
        line=f"{i}, {i**2}, {i**3}"
        f.write(line + "\n")