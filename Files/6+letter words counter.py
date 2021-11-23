import re
with open("big.txt") as f:
    text=f.read()
wordlist=re.findall("\w{6,}", text)
for word in wordlist:
    print(word+"\n")