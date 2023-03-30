def find_second_max_value(ls):
    max_value = ls[0]
    second_max_value = ls[0]

    for element in ls:
        if max_value < element:
            second_max_value = max_value
            max_value = element

        elif second_max_value < element:
            second_max_value = element

    return second_max_value

# ls = [1, 2, 84, 5, 47, 68]
# print(find_second_max_value(ls))
