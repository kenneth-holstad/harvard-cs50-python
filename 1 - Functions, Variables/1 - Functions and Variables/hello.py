# Ask user for their name
name = input("What's your name? ")

# Process input string
# name = name.capitalize() only capitalizes first word
name = name.strip().title()
# you could have done this all in one line name = input("What's your name? ").strip().title()

# Say hello in various ways
print("hello, " + name)
print("hello,", name)

print("hello, ", end='')
print(name)

print(f"hello, {name}")

def hello(to):
    print("hello,", to)

hello(name)

# add a default option to hello()
def hello_def(to="world"):
    print("hello,", to)

hello_def(name)