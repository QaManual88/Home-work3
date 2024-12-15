def simple_calculator():
    print("Hello, I am a simple calculator")
    num1 = int(input("Enter number 1: "))
    operator = input("Enter operator (1 +, 2 -, 3 *, 4 /): ")
    num2 = int(input("Enter number 2: "))

    if operator == '1':
        print(num1 + num2)
    elif operator == '2':
        print(num1 - num2)
    elif operator == '3':
        print(num1 * num2)
    elif operator == '4':
        print(num1 / num2)
    else:
        print("Invalid operator")

def move_last_to_first():
    lst = [1, 2, 3, 4, 5, 6]
    if len(lst) <= 1:
        result = lst
    else:
        result = [lst[-1]] + lst[:-1]
    print(result)  # Результат: [6, 1, 2, 3, 4, 5]

def split_list():
    lst = [1, 2, 3, 4, 5, 6]
    if not lst:
        result = [], []
    else:
        mid = (len(lst) + 1) // 2
        result = [lst[:mid], lst[mid:]]
    print(result)  # Результат: [[1, 2, 3], [4, 5, 6]]

def main():
    print("Choose a program to run:")
    print("1. Simple calculator")
    print("2. Move last element to first")
    print("3. Split list into two")
    choice = input("Enter your choice (1, 2, or 3): ")

    match choice:
        case '1':
            simple_calculator()
        case '2':
            move_last_to_first()
        case '3':
            split_list()
        case _:
            print("Invalid choice, please restart the program and try again.")

if __name__ == "__main__":
    main()









