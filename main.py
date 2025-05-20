# Main.py

import Calc as c

a = int(input("Enter a: "))
b = int(input("Enter b: "))

while True:
    print("\nChoose operation:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("-1: Exit")

    choice = int(input("Enter your choice: "))

    if choice == -1:
        print("Exiting program.")
        break
    elif choice == 1:
        print(f"{a} + {b} = {c.add(a, b)}")
    elif choice == 2:
        print(f"{a} - {b} = {c.sub(a, b)}")
    elif choice == 3:
        print(f"{a} * {b} = {c.mul(a, b)}")
    elif choice == 4:
        result = c.div(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print("Invalid choice. Please try again.")
