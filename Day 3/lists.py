#Start of Day 3

#Lists

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#Access list items by index

print(planets[0])
print(planets[1])

#Length of a list

wonders = ["taj mahal","leaning tower of pisa"]
print(len(wonders))

#Add value to a list
wonders.append("Great Wall of China")
print(len(wonders))

#Remove value from a list
wonders.pop()
print(len(wonders))


#Negative Indexes 

'''Negative indexes start at the end of the list and work backward.'''
print(wonders[-1])
print(wonders[-2])

#Finding value in list
print(planets.index("Venus"))

#Excercise

planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
print(planets)
print("There are", len(planets) ,"planets")
planets.append("Pluto")
print("There are", len(planets), "planets")
print(planets[-1], "is the last planet")


# Floats in List
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 #in Newtons, on earth

print("In Mercury a double decker bus weighs", gravity_on_planets[0]*bus_weight ,"N.")
print("In Venus a double decker bus weighs", gravity_on_planets[1]*bus_weight ,"N.")
print("In Mars a double decker bus weighs", gravity_on_planets[3]*bus_weight ,"N.")
print("In Jupiter a double decker bus weighs", gravity_on_planets[4]*bus_weight ,"N.")
print("In Saturn a double decker bus weighs", gravity_on_planets[5]*bus_weight ,"N.")
print("In Uranus a double decker bus weighs", gravity_on_planets[6]*bus_weight ,"N.")
print("In Neptune a double decker bus weighs", gravity_on_planets[7]*bus_weight ,"N.")

# min() and max()

print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N.")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N.")

#Slice lists [staring index:ending index(+1)]

'''When you use a slice, you create a new list that starts at the starting index and that ends before (and does not include) the ending index.'''

planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

'''A slice creates a new list. It doesn't modify the current list'''

planets_after_earth = planets[3:]
print(planets_after_earth)
print(planets)

#Join lists + 

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

'''Joining lists creates a new list. It doesn't modify the current list.'''

#Sort lists

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Sorting in Reverse Order .sort(reverse=True)

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

'''Using sort modifies the current list.'''

#Excercise

planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
user_planet = input("Please enter the name of the planet with a Capital Letter at initial name\n")
planet_index = planets.index(user_planet)
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])
print("Here are the planets farther than " + user_planet)
print(planets[planet_index+1:])
