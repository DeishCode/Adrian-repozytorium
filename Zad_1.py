
def greetings (name, surname):
    return f"Cześć {name} {surname}"


name = str(input("Input name: "))
surname = str(input("Input surname: "))

print(greetings(name, surname))