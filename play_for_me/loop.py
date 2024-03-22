count = 0
highest = 0
highest_two = 0
while count != -1:
    number = int(input('Enter a number: '))

    if number > highest:
        highest_two = highest
        highest = number
    elif number > highest_two:
        highest_two = number
    count += 1
print(f' Highest is {highest} 2nd highest number is {highest_two}' )
