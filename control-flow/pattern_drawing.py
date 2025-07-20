length = int(input("Enter the size of the pattern: "))
is_active = True


while is_active:
    for row in range(length):
        for column in range(length):
            print("*",end="")
        print()
    is_active = False




