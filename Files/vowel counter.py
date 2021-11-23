import re
text="To be, or not to be, that is the question"
vowelnumber=re.findall("[aeiou]", text)
print(len(vowelnumber))