def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b  
def repl():
    print("Welcome to the Arbitrary Precision Calculator!")
    print("Type 'exit' to quit.")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print(f"You entered: {user_input}")
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Use format: num1 <operator> num2 ")
                continue

            num1, operator, num2 = parts
            num1, num2 = int(num1), int(num2)  # Convert to integers

            if operator == "+":
                print(add(num1, num2))
            elif operator == "-":
                print(subtract(num1, num2))
            elif operator == "*":
                print(multiply(num1, num2))
            elif operator == "/":
                print(divide(num1, num2))
            else:
                print(f"Unknown operator: {operator}")
        except ValueError:
            print("Invalid numbers. Please enter integers.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
