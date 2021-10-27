real_pin="0805"
user_pin=input("Podaj numer pin: ")
for a in range(1,4):
    if user_pin==real_pin:
        print("Correct!")
        break
    elif user_pin != real_pin and a != 3:
        print("Incorrect")
        user_pin=input("Podaj numer pin: ")
    elif a==3:
        print("Your account has been blocked")

