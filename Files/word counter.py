import re
text="To be, or not to be, that is the question"
vowelnumber=re.findall("\w+", text)
print(len(vowelnumber))