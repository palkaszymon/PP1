userinput=input("File name: ")
with open(userinput) as f:
    linecount=0
    while f.readline():
        linecount+=1
    print(f"""Number of lines: {linecount}
File name: {userinput}""")
