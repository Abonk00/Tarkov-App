import csv

print("Death Tracker Beta")

#option for user input and entry
v = input("Ready to add a entry?: ").lower()

if v[0] == "y" :
    test = input("What map did you die on?: ")
    gun = input("What gun were you using?: ")
    reflect = input("What did you learn?: ")
    outcome = input(" Did you survive?: " )

#Saves to CRV file
    with open("tarkovdoc.text", mode = "w") as tarkovdoc:
        tarkov_writer = csv.writer(tarkovdoc, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)


#going to add stats eventually.
elif v[0] == "n":
	overall = input("Do you want to see overall stats?: ")
	

else:
    print("There is no other option at this time.")

print()    