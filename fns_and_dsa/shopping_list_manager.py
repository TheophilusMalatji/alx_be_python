def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            print("-------------Pick item you choose to remove-------------")
            print(shopping_list)
            item = input("Item you wish to remove:  ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not in list")
            pass

        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()