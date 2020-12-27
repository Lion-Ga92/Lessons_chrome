# Chapter 3 concluding exercises

# Section 3-8 

visit_places = ["paris", "antioch", "washington", "volgograd", "japan"]

print(visit_places)
print(sorted(visit_places))
print(sorted(visit_places, reverse=True))
visit_places.reverse()

print(visit_places)

visit_places.sort()
print(visit_places)
visit_places.sort(reverse=True)
print(visit_places)

print(f"i want to visit {len(visit_places)} places")


family_mine = ["alicia", "luis", "dania"]
family_mine.append("luisH")

print(f"my sister is {family_mine[2]}")
print(f"My dad, RIP used to be {family_mine[3]}")

family_mine.insert(1, "mamaNoy")

print(f"my {family_mine[1]} died in 2015 along with dad")

print(family_mine)
print("since they are no longer with us we need to remove them from the list of family")

del family_mine[1]
print(family_mine)

dad_dead = family_mine.pop()
print(dad_dead)
print(family_mine)
print(family_mine[2])