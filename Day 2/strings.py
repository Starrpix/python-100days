#Start of Day2


# String Example
fact = "The Moon has no atmosphere."
print(fact)

#Immutability

fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."

''' It doesn't give concatenated output but fact gives the same "The Moon has no atmosphere." 
Only when a return type is given then the output is displayed'''

fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

# Using quotation marks in string 

moon_radius = "The Moon has a radius of 1,080 miles."
moon_radius = 'The "near side" is the part of the Moon that faces the Earth.'
moon_radius = """ We only see about 60% of the Moon's surface, this is known as the "near side"."""

#Multiline Text

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon:
 There is no atmosphere.
 There is no sound."""


#String Methods

print("temperatures and facts about the moon".title())
'''returns the string in initial caps | Output: Temperatures And Facts About The Moon'''

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

'''Splitting a string'''

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)
'''Output: ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']'''

'''Joining a string'''

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
'''Output: The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year.'''

'''When loading text from data file'''
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)
'''Output: ['Daylight: 260 F', 'Nighttime: -280 F']'''

'''Search from a string'''

print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

'''returns index of the word that is found'''

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars")) #Output : 1
print(temperatures.count("Moon")) #Output : 0

'''returns total number of occurences of a word in a string'''


#Case Conversion

print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())


'''When you're searching for and checking content, a more robust approach is to lowercase a string so that casing doesn't prevent a match.'''

#Check Content

'''processing text to extract information that may appear irregular'''

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

'''incase text is irregular , different splitting methods should be used'''

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

        '''searches for a numeric item and returns the value of it. Note: -70 would be normally returned as False by isnumeric()
        . Like isnumeric(), isdecimal() can also check for strings that looks like decimals'''

 #Extra Validations


print("-60".startswith('-'))

'''helps in verifying the first character of the string'''

print("-30 C".endswith('C'))
'''helps in verifying the last character of string'''

#Transform Text

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))


#String format in Python

'''Percent sign (%) formatting'''

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

'''.format method'''

print("On the Moon, you would weigh about {} of your weight on Earth." .format(mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))


name = 'Ganymede'
planet = 'Mars'
gravity = 1.43

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name = name, planet = planet , gravity = gravity ))


'''To increase readbility of code'''

mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))


'''f strings'''

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

''' round() function '''

print(round(100/7,1))

address = "Random house"
head = f"{address.title()}"
print(head)

