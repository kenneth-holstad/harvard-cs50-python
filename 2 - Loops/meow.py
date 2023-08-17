i = 0
x = int(input("How many?: "))
# while loop
while i < x:
    print("meow")
    i += 1

# for loop
for _ in range(x):
    print("meow")

# pythonic loop
print("meow\n" * x, end="")