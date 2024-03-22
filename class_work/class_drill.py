try:
    number = int(input('Enter a number: '))
    even = 0
    odd = 0
    for num in range(1, number):
        if num % 2 == 0:
            even += num
        else:
            odd += num
    print(f'The sum of even number is {even}', '\n'f'and the sum of odd number is {odd}')
except ValueError:
    print('Invalid entry!')


