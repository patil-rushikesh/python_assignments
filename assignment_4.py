#Assignment 4
numbers = []

while True:
    user_input = input("Enter a number (or 'n' to finish): ")
    if user_input == 'n':
        break
    num = int(user_input)
    numbers.append(num)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

numbers_dict = {
    'even': even_numbers,
    'odd': odd_numbers
}

print(numbers_dict)
