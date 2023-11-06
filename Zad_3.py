
def even_number (num):
    return num % 2 == 0


result = even_number(int(input("Input number: ")))

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
