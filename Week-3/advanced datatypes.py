 #advanced data types

#mutable vs immutable

#Mutable are data that can change during program life cycle
#add/ remove elements
#Immutable--> data types that can't be edited

#1 list (mutable)

friends = ("ricco", "precious", "jeff" )
print(friends)
#or friends = [] for empty list
#add-->append(), extend()


students = ("shawn", "austin", "Lily")
friends.extend(students)
friends.append("alvin")
friends.sort()
friends,reverse()
print(friends)

#2]Tuples(Immaculate)
#Type of list that are immutable

stationarys = ("pens", "pencils",)
#replace the whole tuple
stationarys = ("ruler","pen")
print(stationarys)
#for stationarys in stationarys:
for stationary in stationarys:
    print(stationary)

    #numbers = (1,2,3,4,5)
#3)Dictionaries aka dict
#dictionaries uses key and value pair
student = {"name" : "Khabib","age":27,"gender":"male","is_tall":True}
#"name" : "Bob" --->name(key) bob(value)
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])
print(student.values())
print(student.keys())

friend = {"fav_color" : "black","hobby" : "reading", "course": "computing", "weight": 130,"height":250}
print(friend["fav_color"])
print(friend["hobby"])
print(friend["course"])
print(friend["weight"])
print(friend["height"])
print(friend)
print(friend.values())
print(friend.keys())
















print(student["Name"])
print(student["age"])
print(student["gender"])
print(student["height"])

friend = ("Fav color: "Black")