"""expenses = []
print("everyday expense tracker")
user = int(input("1.add expense\n2.view expenses\n3.exit \n "))
while user == 1 or 2 or 3:
    if user == 1:
        amount = int(input("enter your expense:"))
        category = input("enter your expense category:")
        description = input("enter your expense description:")
    elif user == 2:
        print(amount)
        print(category)
        print(description)
    else:
        print("your expense has been calculated")
print("enther either 1 to add expense 2 to view your currernt expense and 3 to exit form the expense calculator")
        

        """

expenses = []
print("everyday expense tracker")
while True:
    user = int(input("1.add expense\n2.view expenses\n3.exit \n "))
    if user == 1:
        expense = {}
        expense["amount"] = int(input("enter your expense:"))
        expense['category'] = input("enter your expense category:")
        expense['description'] = input("enter your expense description:")
        expenses.append(expense)
        print('expense added successfully')
    elif user == 2:
        for expense in expenses:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
    elif user == 3:
        print("your expense has been calculated and you have exited the expense calculator")
        break
    else:
        print("enter either 1 to add expense, 2 to view your current expenses, or 3 to exit from the expense calculator")


