# with good general code conventions
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n    # don't forget to return value


def meow(n):
    for _ in range(n):
        print("meow")