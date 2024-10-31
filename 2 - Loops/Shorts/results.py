results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

print(results)

results.append(["Bowser", "Donkey Kong Jr."]) # note: this creates a sublist within the list which is likely not desired
results.remove(["Bowser", "Donkey Kong Jr."])
results.extend(["Bowser", "Donkey Kong Jr."]) # instead, this extends the existing list

print(results)

results.remove("Bowser") # removes first instance of match

print(results)

results.insert(0, "Bowser") # inserts at index 0

print(results)

print(results.index("Mario"))

results.reverse()

print(results)