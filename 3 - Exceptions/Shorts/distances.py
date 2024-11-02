# similar concept to same file from section 2

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")

    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
# of course you could set up a way to extract the number... although that would be going by specific case

    m = convert(au)
    print(f"{m} m")


def convert(au):
    return au * 149597870700
# note: this * operator if you apply it to text repeats the next that many times
# i.e. 63 * a lot = 636363636363636363....
# so this causes a memory error in this case. Handle via type conversion above

main()