#create a list of empty  favourite musicians 
#using a for loop add new musicians 
#copy the list called celebrities
#sort the list 
#pop out two celebrities
#count the remaining celebrities 

favourite_musicians = ["Dababy", "Polo G", "Drake","21 savage" ,"Rema" ]
for musician in favourite_musicians:
    print(musician)
favourite_musicians.append ("Cardi B")
favourite_musicians.append("Dax")
favourite_musicians.append("J cole")
favourite_musicians.append("Playboi carti")
favourite_musicians.append("Lil Tjay")
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