import os, time

todo_list = []

def ppp():
    time.sleep(1)
    os.system("clear")

def print_menu():
    print("\nTodo List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Edit item")
    print("4. View list")
    print("5. Exit")

def add_item(todo_list):
    item = input("Enter the item to add: ")
    if item not in todo_list:
        todo_list.append(item)
        print("Item added successfully!")
    else:
        print("Item already exists in the list.")

def remove_item(todo_list):
    view_list(todo_list)
    item = input("Enter the item to remove: ")
    if item in todo_list:
        confirm = input(f"Are you sure you want to remove '{item}'? (y/n): ")
        if confirm.lower() == "y":
            todo_list.remove(item)
            print("Item removed successfully!")
    else:
        print("Item not found in the list.")

def edit_item(todo_list):
    view_list(todo_list)
    item = input("Enter the item to edit: ")

    if item in todo_list:
        new_item = input("Enter the new item: ")
        index = todo_list.index(item)
        todo_list[index] = new_item
        print("Item edited successfully!")
    else:
        print("Item not found in the list.")

    #what is this?

def view_list(todo_list):
    print("Todo List:")
    if len(todo_list) == 0:
        print("No items in the list.")
    else:
        for item in todo_list:
            print(item)



while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_item(todo_list)
        ppp()
    elif choice == "2":
        remove_item(todo_list)
        ppp()
    elif choice == "3":
        edit_item(todo_list)
        ppp()
    elif choice == "4":
        view_list(todo_list)
        print("\nItems will close in 5 seconds")
        time.sleep(5)
        os.system("clear")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
        ppp()

print("Exiting Todo List Manager. Goodbye!")
