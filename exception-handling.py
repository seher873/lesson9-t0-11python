#Exception Handling 
try:
    num = int(input("Enter your number: "))
    print(10 / num)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
