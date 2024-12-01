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
