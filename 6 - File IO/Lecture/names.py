# To pre-process a file (in this case, sort) - you do something like this

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

'''
# Even more compact but harder to modify:
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

'''