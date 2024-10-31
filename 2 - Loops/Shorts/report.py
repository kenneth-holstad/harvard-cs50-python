def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

# get function gives return value if null to prevent Key Error
# note the area in """ """ is NOT a comment because it is inside return function here
# you have to be careful with that - """ """ does not explicitly create comments
# python simply ignores these kind of text if they aren't a part of something
def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """


main()