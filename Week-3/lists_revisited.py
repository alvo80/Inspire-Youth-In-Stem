#!/usr/bin/env python3

myFavouriteFruits = ["banana","apple","mango","lime","avocado"]

for fruit in myFavouriteFruits:
    print(fruit)

print(len(myFavouriteFruits))

friends = ["Tado","Zolo","Mutiah","Leon","Jeff"]
print(friends)
friends[0] = "Tado"
print(friends)
print("-----------------------------------------------------")
new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)

