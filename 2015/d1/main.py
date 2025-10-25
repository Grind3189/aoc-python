# --- Day 1: Not Quite Lisp ---


def p1(input):
    floor = 0
    for char in content:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    print(f"Final floor: {floor}")


def p2(input):
    floor = 0
    position = 0

    for i, char in enumerate(content):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            position = i
            break

    print(f"First character position that causes santa to basement: {position}")


try:
    with open("input.txt", "r") as file:
        content = file.read().strip()

        p1(content)
        p2(content)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print(f"An error occured: {e}")
