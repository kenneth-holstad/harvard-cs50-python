import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        sys.exit("dummy")
    print(args[0])
    [a,b] = args
    print(a)
    print(b)
    print(sys.argv[0])

main()