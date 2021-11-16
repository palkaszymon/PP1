def occurs(number,array):
    if number in array:
        return True
    else:
        return False

number=int(input("Type in a number to check:"))
array=[15,38,7,23,14]

if occurs(number, array)==True:
    print(f"""Number: {number}
Array: {array}
Result: number {number} appears in the array""")
else:
    print(f"""Number: {number}
Array: {array}
Result: number {number} does not appear in the array""")