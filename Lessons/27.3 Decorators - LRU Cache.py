"""LRU (Least Recently Used) cache decorator is a utility that helps to cache the results of a function/method, 
storing only a limited number of results based on the most recently used principle."""

from functools import cache, lru_cache


@lru_cache(maxsize=5)  # or @cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(400):
        print(i, fib(i))
    print("done")


if __name__ == "__main__":
    main()
