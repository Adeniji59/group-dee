num = int(input("enter set_of_numbers :"))

reversed_num = 0


def reverse_func(num):
    global reversed_num

    while num > 0:
        r = num % 10
        reversed_num = (reversed_num * 10) + r
        num = num // 10


reverse_func(num)
print("Revered of Entered number is =", reversed_num)
