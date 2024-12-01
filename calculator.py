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

if __name__ == "__main__":
    repl()
