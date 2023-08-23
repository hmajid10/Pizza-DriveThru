print("Welcome to Vienna, VA Pizza Corner! ")
size = input("What's the size of the pizza you want to order? S, M or L ")
add_pepperoni = input("Due you want to add pepperoni? Y or N ")
extra_cheese = input("Due you want to add extra cheese? Y or N ")

# Main code
if size == "S":
    Bill = 15
    if add_pepperoni == "Y":
        Bill += 2
        if extra_cheese == "Y":
            Bill += 1
        print(f"Your total bill is: ${Bill}.")
    else:
        if extra_cheese == "Y":
            Bill += 1
        print(f"Your total bill is: ${Bill}.")
elif size == "M":
    Bill = 20
    if add_pepperoni == "Y":
        Bill += 3
        if extra_cheese == "Y":
            Bill += 1
        print(f"Your total bill is: ${Bill}.")
    else:
        if extra_cheese == "Y":
            Bill += 1
        print(f"Your total bill is: ${Bill}.")
else:
    Bill = 25
    if add_pepperoni == "Y":
        Bill += 3
        if extra_cheese == "Y":
            Bill += 1
        print(f"Your total bill is: ${Bill}.")
    else:
        if extra_cheese == "Y":
            Bill += 1
            print(f"Your total bill is: ${Bill}.")