#create a list of empty  favourite musicians 
#using a for loop add new musicians 
#copy the list called celebrities
#sort the list 
#pop out two celebrities
#count the remaining celebrities 

favourite_musicians = ["Santan Dave", "Polo G", "Central Cee","A2 anti" ,"Burna Boy" ]
for musician in favourite_musicians:
    print(musician)
favourite_musicians.append ("Popcaan")
favourite_musicians.append("K-trap")
favourite_musicians.append("Tion Wayne")
favourite_musicians.append("Polo G")
favourite_musicians.append("Vybz Kartel")
for musician in favourite_musicians:

    print(musician)

celebs = favourite_musicians.copy()
print(celebs)
celebs.sort()
print(celebs)

celebs.pop()
celebs.pop()
print(celebs)


print(len(celebs))