# Exercise 2: File Handling

filename = "notes.txt"

try:
    # 1. Ask user for message
    message = input("Enter a short note/message: ")

    # Save message (write mode)
    with open(filename, "w") as file:
        file.write(message + "\n")

    print("\nSaved successfully!")

    # 2. Read file
    print("\nReading file...")
    with open(filename, "r") as file:
        print(file.read())

    # 3. Append new data
    new_message = input("\nEnter another note: ")

    with open(filename, "a") as file:
        file.write(new_message + "\n")

    print("\nAppended successfully!")

    # Show updated content
    print("\nUpdated content:")
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found!")