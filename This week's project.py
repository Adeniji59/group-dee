numbers = input("Enter the set of number :-")

def sum(numbers):
    total = 0
    for x in numbers:
        total += int(x)
    return total
print(sum(numbers))