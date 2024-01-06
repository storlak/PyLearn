# args and kwargs together.
# args take non-keywırd kwargs take keywords arguments


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


shipping_label(
    "Dr",
    "SpongeBob",
    "SquarePants",
    "III",
    street="125 Fake St",
    apt="100",
    city="Detroit",
    State="MI",
    zip="54321",
)
