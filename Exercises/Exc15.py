import random
from sty import fg


def generateRGB():
    red = random.randint(0, 256)
    blue = random.randint(0, 256)
    green = random.randint(0, 256)
    return red, blue, green


red, blue, green = generateRGB()
print(red, blue, green)
