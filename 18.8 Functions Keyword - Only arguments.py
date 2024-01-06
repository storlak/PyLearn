# args into a tuple - kwargs into a dictionary
def func(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)


# if we do not precise c we'll get a TypeError: missing 1 required item
func(10, 20, 30, 40, c=50)  # we have to prcesie c bcs it is not a positional argument.


def func1(a, b=2, c=3, *, d=10, e, f=30):
    print(a, b, c, d, e, f)


# a positional, b&c defaulted to to and 3. d defaulted to 10. e defaulted to 20. f defaulted to 30
func1(1, e=20)


def coords_to_json(
    *, longtitude, latitude
):  # we use * to force using named arguments!!! no positional arguments bsc there is *
    return f'{{"longtitude": {longtitude},"latitude":{latitude} }}'


coords_to_json(
    longtitude=10, latitude=20
)  # bcs of start we have to use named arguments. longt and lat must be named.
