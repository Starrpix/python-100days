#Start of Day 4

#Functions with no arguments

'''you use the def keyword followed by a name, parentheses, and then the body with the function code'''

def rocket_parts():
    return "payload,prepellent,structure"
output = rocket_parts()

print(f"The output is {output}")

#Required arguments

'''any() takes an iterable (for example, a list) and returns True if any item in the iterable is True. Otherwise, it returns False.'''

any("True,False,False") # Output : True
any("False,False") # Output : False

#Optional arguments

'''str() creates a string from an argument. If no argument is passed in, it returns an empty string'''

str(20)

#Functions with arguments

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    

print(distance_from_earth("Moon"))    

#Multiple Required Arguments

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

#Function as Arguments

print(round((days_to_complete(238855, 75)))) #hours,miles

#Excercise: Report Generation

def generate_report(main_tank,external_tank,hydrogen_tank):
    output = f"""Fuel report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """
    print(output)

generate_report(80,70,50)

#Keyword Arguments

'''Keyword argument values must be defined in the functions themselves'''

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()       #datetime module to define the current time
    arrival = now + timedelta(hours=hours)  #timedelta to allow the addition operation that results in a new time object.
    return arrival.strftime("Arrival: %A %H:%M") 

'''print(arrival_time(hours=20))'''
print(arrival_time())

#Mixed Arguments and Keyword Arguments

from datetime import timedelta, datetime

def arrival_time(destination,hours=51):
    now = datetime.now()       #datetime module to define the current time
    arrival = now + timedelta(hours=hours)  #timedelta to allow the addition operation that results in a new time object.
    return arrival.strftime(f" Arrival To {destination} : %A %H:%M") 

print(arrival_time("Moon",))


#Variable Arguments

def sequence_time(*args):
    total_minute = sum(args)
    if total_minute<60:
        return (f"The launch has {total_minute} minutes.")
    else:
        return (f"The launch has {total_minute/60} hours.")


print(sequence_time(23,11,11))


#Variable Keyword Arguments

def fuel_report(**fuel_tank):
    for name,value in fuel_tank.items():
        print(f'{name}: {value}')

 
fuel_report(main=50,external=20,hydrogen=30)

