import random

cards = ["jack", "queen", "king"]


def main():
    # print(random.choices(cards, weights=[100, 0, 0], k=2)) # rigged
    random.seed(0) # this sets consistent seed - useful for debugging
    print(random.sample(cards, k=2))


main()