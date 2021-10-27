from typing import Counter


print("Enter numbers to get the quantity, sum and mean of them, type 0 to stop the program and get your results")
quantity=0
sum=0
number=int(input("Enter number: "))
while number != 0:
    sum=sum+number
    quantity=quantity+1
    number=int(input("Enter number: "))
    if number == 0:
        print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean=:{int(sum/quantity)}")
        break