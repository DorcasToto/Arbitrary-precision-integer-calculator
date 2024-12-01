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

def string_subtract(num1, num2):
    """
    Subtracts two numbers represented as strings.
    Assumes num1 >= num2 for simplicity.
    """
    # Determine if result will be negative
    is_negative = False
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        num1, num2 = num2, num1
        is_negative = True

    num1, num2 = num1[::-1], num2[::-1]  
    result = []
    borrow = 0

    for i in range(len(num1)):
        digit1 = int(num1[i]) 
        digit2 = int(num2[i]) if i < len(num2) else 0  
        diff = digit1 - digit2 - borrow
        if diff < 0:
            diff += 10 
            borrow = 1
        else:
            borrow = 0
        result.append(diff)

   
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    
    final_result = ''.join(map(str, result[::-1]))
    return f"-{final_result}" if is_negative else final_result

def string_multiply(num1, num2):
    """
    Multiplies two numbers represented as strings.
    """
    num1, num2 = num1[::-1], num2[::-1]
    result = [0] * (len(num1) + len(num2)) 

    # Perform multiplication
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            product = digit1 * digit2
            result[i + j] += product  
            result[i + j + 1] += result[i + j] // 10 
            result[i + j] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))

def string_divide(num1, num2):
    """
    Divides two numbers represented as strings and returns the quotient as a string.
    """
    if num2 == "0":
        return "Error: Division by zero"

    if num1 == "0":
        return "0"

    quotient = []
    remainder = 0

    for digit in num1:
        remainder = remainder * 10 + int(digit)
        quotient_digit = remainder // int(num2)
        quotient.append(str(quotient_digit))
        remainder = remainder % int(num2)

    # Remove leading zeros
    quotient = ''.join(quotient).lstrip("0")
    return quotient if quotient else "0"

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

            if operator == "+":
                if len(num1) > 18 or len(num2) > 18:  
                    print(f"Result: {string_add(num1, num2)}")
                else:
                    print(f"Result: {add(int(num1), int(num2))}")
            elif operator == "-":
                if len(num1) > 18 or len(num2) > 18:  
                    print(f"Result: {string_subtract(num1, num2)}")
                else:
                    print(f"Result: {subtract(int(num1), int(num2))}")
            elif operator == "*":
                if len(num1) > 18 or len(num2) > 18:
                    print(f"Result: {string_multiply(num1, num2)}")
                else:
                    print(f"Result: {multiply(int(num1), int(num2))}")
            elif operator == "/":
                if len(num1) > 18 or len(num2) > 18:
                    print(f"Result: {string_divide(num1, num2)}")
                else:
                    print(f"Result: {divide(int(num1), int(num2))}")
            else:
                print(f"Unknown operator: {operator}")
        except ValueError:
            print("Invalid numbers. Please enter integers.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
