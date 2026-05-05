def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

my_list = [3, 9, 1, 5, 5]
print(sum_list(my_list))
