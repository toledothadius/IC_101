records = {}
name = input("Name: ")
print("Hello ",name)
print ("pls type (add) if you want to add, (del)if you want to delete, and (end) if you want to end the program")


while True:
    choice = input("What do you want to do: ")

    if choice == "add":
        key = input("Key: ")
        value = input("Value: ")
        records[key] = value
        print(records)

    elif choice == "del":
        key = input("Key: ")
        del records[key]
        print(records)


    elif choice == "end":
            print ("Thank You!!!!")
            break

    else:
        print("Invalid Please try again!!!")