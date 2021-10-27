amount=int(input("Enter the amount in PLN: "))
piatki=amount//5
dwojki=(amount-(piatki*5))//2
jedynki=amount-(piatki*5)-(dwojki*2)
print(f"""The amount of PLN {amount} in coins: 
5 zł - {piatki}
2 zł - {dwojki}
1 zl - {jedynki}""")
