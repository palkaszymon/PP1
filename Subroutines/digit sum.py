def digitsum(n):
    sum=0
    for digit in str(n):
        sum+=int(digit)
    return sum
print(digitsum(7182))
