def add(int1, int2):
    return int1 + int2

def subtract(int1, int2):
    return int1 - int2

def multiply(int1, int2):
    return int1 * int2

def divide(int1, int2):
    return int1 / int2

print("Please choose an arithmetic operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        interger1 = float(input("Enter first interger: "))
        interger2 = float(input("Enter second interger: "))

        if choice == '1':
            print(interger1, "+", interger2, "=", add(interger1, interger2))

        elif choice == '2':
            print(interger1, "-", interger2, "=", subtract(interger1, interger2))

        elif choice == '3':
            print(interger1, "*", interger2, "=", multiply(interger1, interger2))

        elif choice == '4':
            print(interger1, "/", interger2, "=", divide(interger1, interger2))
        break
    else:
        print("Invalid Choice")