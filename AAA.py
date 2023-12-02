print("Type one of the following: help, start, stop, quit")
command = ""
mode = "stop"
while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if mode == "stop":
            print("Car started...Ready to go!")
            mode = ("start")
        else:
            print("error")

    elif command == "stop":
        if mode == "start":
            print("Car stopped.")
            mode = ("stop")
        else:
            print("error")

    elif command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit''')
    else:
        print("I don't understand that...")
