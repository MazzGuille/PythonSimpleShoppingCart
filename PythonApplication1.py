Shopping_Cart = []
Price = []
loop = True
while loop:
    print(
        "Please select an option. Remember! If your purchase is of 100 or higher, you get a 10% discount!:"
    )
    print("1- Add a new item")
    print("2- Show all items")
    print("3- Remove item")
    print("4- Compute total")
    print("5- Quit")
    answer = int(input())
    if answer == 1:
        print("Please enter the item name:")
        Answer1 = input()
        Shopping_Cart.append(Answer1)
        print(f"What is the price of {Answer1}")
        Answer2 = float(input())
        print(f"How many {Answer1}s will you purchase?")
        Answer3 = int(input())
        Answer4 = Answer2 * Answer3
        Price.append(Answer4)
        loop = True
    elif answer == 2:
        for i in range(len(Shopping_Cart)):
            print(f"{Shopping_Cart[i]} - {Price[i]}")
        if len(Shopping_Cart) == 0 and len(Price) == 0:
            print("No items in cart")
            loop = True
        loop = True
    elif answer == 3:
        print("Wich item would you like to remove?")
        Delete = int(input())
        Shopping_Cart.pop(Delete - 1)
        Price.pop(Delete - 1)
        loop = True
    elif answer == 4:
        Total = sum(Price)
        if Total < 100:
            print(
                "Your purchase does not apply for our discount, if you wish, you could add more items!"
            )
            print(Total)
            loop = True
        elif Total >= 100:
            print("Great! Your purchase applies for our special discount!")
            print(Total - (Total / 10))
            loop = True
    elif answer == 5:
        loop = False
    # elif answer != int:
    # print("Invalid input")
    # loop = True
    else:
        print("Invalid input")
        loop = True

print("Thank you for shopping with us!")
