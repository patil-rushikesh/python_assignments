def find_max(*args):
    if not args:
        return None

    max_number = args[0]
    for number in args:
        if number > max_number:
            max_number = number
    return max_number

def find_min(*args):
    if not args:
        return None

    min_number = args[0]
    for number in args:
        if number < min_number:
            min_number = number
    return min_number

def calculate_average(*args):
    if not args:
        return None

    total = sum(args)
    average = total / len(args)
    return average

user_input = input("Enter a tuple of numbers separated by commas: ")
numbers_list = [int(num) for num in user_input.split(',') if num.strip().isdigit()]
numbers_tuple = tuple(numbers_list)

maximum = find_max(*numbers_tuple)
if maximum is not None:
    print("The maximum number among the given tuple values is:", maximum)
else:
    print("No valid tuple values provided.")

minimum = find_min(*numbers_tuple)
if minimum is not None:
    print("The minimum number among the given tuple values is:", minimum)
else:
    print("No valid tuple values provided.")

average = calculate_average(*numbers_tuple)
if average is not None:
    print("The average of the given tuple values is:", average)
else:
    print("No valid tuple values provided.")
