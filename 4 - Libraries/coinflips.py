import random

x = int(input("How many coinflips?: "))
heads = 0
tails = 0

for i in range(x):
    result = random.choice(["heads", "tails"])
    if result == "heads":
        heads += 1
    else:
        tails += 1

print(f"Total: {heads} Heads, {tails} Tails")