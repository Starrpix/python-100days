#Start of Day 3

#While
user_input = ''
input_list = []
while user_input.lower() != "done":
    
    if user_input:
        input_list.append(user_input)

user_input = input("Enter input or 'done' when done\n")

'''if statement inside the while loop. This statement tests for a string value inside user_input.'''

#For

countdown = [5,4,3,2,1,0]
for count in countdown:
    print(count)


from time import sleep

countdown = [4, 3, 2, 1, 0]

for number,count in countdown:
    print(number)
    print(count)
    sleep(1)  # Wait 1 second , delays by 1 seconds
print("Blast off!! 🚀")    