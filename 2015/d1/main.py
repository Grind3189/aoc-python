# --- Day 1: Not Quite Lisp ---

try:
    with open("input.txt", "r") as file:
        content = file.read().strip()

        floor = 0
        for char in content:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

        print(f"Floor: {floor}")
except FileNotFoundError:
    print("File not found")

except Exception as e:
    print(f"An error occured: {e}")
