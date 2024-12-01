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
def string_add(num1, num2):
    """
    Adds two numbers represented as strings.
    """
    num1, num2 = num1[::-1], num2[::-1]  
    carry = 0
    result = []

    for i in range(max(len(num1), len(num2))):
        digit1 = int(num1[i]) if i < len(num1) else 0
        digit2 = int(num2[i]) if i < len(num2) else 0
        total = digit1 + digit2 + carry
        result.append(total % 10)  
        carry = total // 10      

    if carry:
        result.append(carry)

    return ''.join(map(str, result[::-1]))  

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
            # num1, num2 = int(num1), int(num2)  # Convert to integers

            if operator == "+":
                if len(num1) > 18 or len(num2) > 18:  # Arbitrary threshold for "large" numbers
                    print(f"Result: {string_add(num1, num2)}")
                else:
                    print(f"Result: {add(int(num1), int(num2))}")
            elif operator == "-":
                print(f"Result: {subtract(int(num1), int(num2))}")
            elif operator == "*":
                print(f"Result: {multiply(int(num1), int(num2))}")
            elif operator == "/":
                print(f"Result: {divide(int(num1), int(num2))}")
            else:
                print(f"Unknown operator: {operator}")
        except ValueError:
            print("Invalid numbers. Please enter integers.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
