"""PYTHON CRASH COURSE BOOK SECTION EXERCISES"""

#  Section 3-4 assignment 

guests = ["Young", "John", "Cody"]

print(f"Hello Mrs. {guests[0]} you are formally invited to my dinner party")

print(f"Hello {guests[2]} you are formally invited to my dinner party")

print(f"Hello {guests[1]} you are formally invited to my dinner party")

print(f"{guests[2]} can't come")

#3-5

guests[2] = "Alice"

print(f"{guests[2]} you are now invited" )
print(guests)

#3-6 
print("Hey guys!!! We have more room now!!!")

guests.insert(0, "Antoine")
guests.insert(2, "Smitty")
guests.append("Tom")
print(guests)

for x in guests:
    print(f"hello {x} you are invited to dinner")

# ^^^^^^^^^^^^^^^^^^^^^^^^
# YAY MY FIRST LOOP AFTER MY HOSPITAL STAY!!!!

remove_1 = guests.pop()

print(f"hello {remove_1} i regret to cancel")

remove_2 = guests.pop()

print(f"hello {remove_2} i regret to cancel")

remove_3 = guests.pop()

print(f"hello {remove_3} i regret to cancel")

remove_4 = guests.pop()

print(f"hello {remove_4} i regret to cancel")

print(guests)

for x in guests:
    print(f"Hello {x}")

del guests[0]

del guests[0]

print(guests)

