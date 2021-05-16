def check(num):
    if num == 0:
        print("Zero")
    elif num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Invalid input")


num = input("Enter a number")
check(num)
