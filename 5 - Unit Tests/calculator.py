# Tests a function with multiple functions via pytest


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n # break this if you want to test


if __name__ == "__main__":
    main()