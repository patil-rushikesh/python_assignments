def find_min(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value

def find_max(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value

def calculate_mean(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    return sum(numbers) / len(numbers)

def main():
    # Accept numbers from the user
    input_numbers = input("Enter numbers separated by space: ")
    number_list = [float(num) for num in input_numbers.split()]

    # Calculate minimum, maximum, and mean
    minimum = find_min(number_list)
    maximum = find_max(number_list)
    mean = calculate_mean(number_list)

    # Display the results
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Mean: {mean}")

if __name__ == "__main__":
    main()
