#Start of Day 2

#Addition
answer = 30 + 12
print(answer)

#Subtraction
result = 30 - 12
print(result)

#Multiplication
product = 30 * 12
print(product)

#Division
quotient = 30 / 12
print(quotient)

#Floor Division
seconds = 1042
display_minutes = seconds // 60

'''Output : 17 | Rounds up or Rounds down'''

#Modulo Division
display_seconds = seconds % 60 
print(display_minutes)
print(display_seconds)

#Order of Operation

'''PEMDAS
Parentheses
Exponents
Multiplication and division
Addition and subtraction'''


#Program that calculates distance between two planets

first_planet = 149597870 # Earth to Sun
second_planet = 778547200 # Jupiter to Sun
distance_km = second_planet - first_planet
print(distance_km)
distance_mi = distance_km / 1.609344
print(distance_mi)

#Conversions

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

#Absolute Value

print(abs(39 - 16))
print(abs(16 - 39))

#Rounding

print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))

#Math Library

from math import ceil,floor

round_up = ceil(1.5)
round_down = floor(1.4)
print(f"{round_up} {round_down}")

