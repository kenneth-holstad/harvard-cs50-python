# enable working with float
x = float(input("X?"))
y = float(input("Y?"))

z = round(x + y)
z = round(x / y, 2)

print(z)

"""
alternate method
z = x / y
print(f"{z:.2f}")
"""