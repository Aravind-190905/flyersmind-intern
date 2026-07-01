try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("You don't have permission to open this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")