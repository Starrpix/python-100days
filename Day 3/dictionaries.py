#Start of Day 3

#Dictionary
'''A dictionary is a collection of key/value pairs'''

planet = {
    'name': 'Earth',
    'diameter' : {
        'equator' : 2323,
        'topography' : 432
    },
    'moons': 1
}

'''keys : name & moon , value : 'Earth' & 1'''

#Read Dictionary Values

print(planet.get('name')) #if key isn't available .get returns None
print(planet['moons']) #if key isn't available it raises a KeyError.

#Modify a Dictionary

planet.update({'name' : 'Venus'})
print(planet['name'])

planet['name'] = 'Jupiter'
print(planet['name'])

planet.update({
    'name': 'Neptune',
    'moons': 3
})

print(planet['name'])


#Add and Remove Keys

planet['orbit'] = 1234
print(planet['orbit'])

planet.pop('orbit')

#Nested Dictionaries

planet['diameter(km)'] = {
    'polar': 1234,
    'equatorial' : 2432
}

planet = {
    'name': 'Earth',
    'diameter' : {
        'equator' : 2323,
        'topography' : 432
    },
    'moons': 1
}

print(planet['diameter']['equator'])


#Excercise

planet = {
    'name': 'Mars',
    'moons': 2
}
print(f"{planet['name']} has {planet['moons']} moons(s)")
planet['circumference (km)'] = {
    'polar' : 6572,
    'equatorial' : 6792
}

print(f"{planet['name']} has polar circumference of {planet['circumference (km)']['polar']}")

#Dynamic Programming with Dictionaries

'''The keys() method returns a list object that contains all the keys'''
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f"{key} : {rainfall[key]}cm")

#Determine if a key exists in a dictionary 

if 'december':
    rainfall['december'] = rainfall['december'] + 1
    print(rainfall['december'])
else:
    rainfall['december'] = 1 

#Retrieve all the values
'''values() returns the list of all values in a dictionary without their respective keys.'''

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

    print(total_rainfall)


    #Excercise

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
total_planets = len(planet_moons.keys())
total_moons = 0
for moon in moons:
    total_moons += moon

average = total_moons / total_planets    
print(f"Each planet has average of moons {average} moons")

