# show general scripting convention
# also add conditional to allow default behavior
def main():
    name = input("Name? " )
    if name.strip() == "":
        hello()
    else:
        hello(name)

# note that you CANNOT call name in this function because main() exists only in main()
def hello(to="world"):
    print("hello,", to)

main()