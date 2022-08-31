def add(a,b):
    answer = a + b
    print(f"{str(a)} + {str(b)} = {str(answer)}" + "\n")

def multiply(a,b):
    answer = a * b
    print(f"{str(a)} x {str(b)} = {str(answer)}" + "\n")

def minus(a,b):
    answer = a - b
    print(f"{str(a)} - {str(b)} = {str(answer)}" + "\n")

def divide(a,b):
    answer = a / b
    print(f"{str(a)} / {str(b)} = {str(answer)}" + "\n")

def quit():
    print('Program ended!')

while True:
    print("A. Multiply")
    print("B. Add")
    print("C. Minus")
    print("D. Divide")
    print("E. Exit")

    choice = input("Please choose the calculation: ")

    if choice == 'a' or choice == 'A':
        a = int(input("1st number: "))
        b = int(input("2nd number: "))
        multiply(a,b)
    elif choice == 'b' or choice == 'B':
        a = int(input("1st number: "))
        b = int(input("2nd number: "))
        add(a,b)
    elif choice == 'c' or choice == 'C':
        a = int(input("1st number: "))
        b = int(input("2nd number: "))
        minus(a,b)
    elif choice == 'd' or choice == 'D':
        a = int(input("1st number: "))
        b = int(input("2nd number: "))
        divide(a,b)
    elif choice == 'e' or choice =='E':
        quit()
        break
    else:
        print("Invalid Choice! Please choose again!" + "\n")