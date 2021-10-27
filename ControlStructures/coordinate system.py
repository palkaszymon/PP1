x=int(input("Podaj koordynat x: "))
y=int(input("Podaj koordynat y: "))
if x>0 and y>0:
    print("Point P lies in the 1st quadrant of the coordinate system: ")
elif x<0 and y>0:
    print("Point P lies in the 2nd quadrant of the coordinate system: ")
elif x<0 and y<0:
    print("Point P lies in the 3rd quadrant of the coordinate system: ")
elif x>0 and y<0:
    print("Point P lies in the 1st quadrant of the coordinate system: ")
