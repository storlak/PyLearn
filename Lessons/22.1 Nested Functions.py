def say_hello(name):
    def prefix():
        return "Hello, "

    msg = prefix() + name
    return msg


name_to_greet = "John"
greeting_message = say_hello(name_to_greet)
print(greeting_message)
