with open("MeatAndFish.txt") as mnf, open("GrainsAndBread.txt") as gab, open("shoppinglist.txt", "w") as list:
    text=mnf.read()
    list.write(text + "\n")
    text=gab.read()
    list.write(text)