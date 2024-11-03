# Function to be tested
'''
def main():
    name = input("What's your name? ")
    hello(name)


# this is not ideal because it produces a side effect so we will change this

def hello(to="world"):
    print("hello,", to)
'''

# Has function return a str instead
def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()