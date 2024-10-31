distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU ({convert(distances[name])} m) from Earth")

'''
alternative method 1 - iterate by values (note: this does not pass on the names so I don't like it):
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")

a way to force the above to work with displaying names just for fun:
names = list(distances.keys())
for i, distance in enumerate(distances.values()):
    print(f"{names[i]} is {distance} AU ({convert(distance)} m) from Earth")

alternative method 2 - iterate by items:
    for name, distance in distances.items():
        print(f"{name} is {distance} AU ({convert(distance)} m) from Earth")

'''

def convert(au):
    return au * 149597870700

main()