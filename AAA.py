print("Type one of the following: help, start, stop, exit")
command = ""
while command != "quit":
    command = input("> ").lower()

    if command == "start":
        print("Car started...Ready to go")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit''')
    else:
        print("I don't understand that...")
