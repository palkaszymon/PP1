a=int(input("Podaj długość boku a: "))
b=int(input("Podaj długość boku b: "))
c=int(input("Podaj długość boku c: "))
p=(1/2)*(a+b+c)
area=(p*(p-a)*(p-b)*(p-c))**(1/2)
print(f"Pole trójkąta ABC wynosi: {area}")
