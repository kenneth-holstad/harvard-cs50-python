def main():
    x = int(input("X?"))
    print("x squared is", square(x))

def square(n):
    return(n ** 2)
# alt: return n * n or return pow(n, 2)
# see the parens aren't actually needed for return

main()