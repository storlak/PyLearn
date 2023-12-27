import string

alphabet = set(string.ascii_letters)
text = "The quick brown fox jumps over the lazy dog"

print(set(string.ascii_letters.casefold()) - set(text.casefold()))
