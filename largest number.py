def find_largest_number(numbers):
    if not numbers:
        return None  # Return None for an empty list

    largest = numbers[0]  # Assume the first number is the largest

    for number in numbers:
        if number > largest:
            largest = number

    return largest

# Example usage:
number_list = [6 , 4 ,7 , 8 , 9 , 2]
largest_number = find_largest_number(number_list)
print("The largest number is:", largest_number)
