

def unique_and_cubed_list (list_1, list_2):
    combined_list = list_1 + list_2
    unique_list = list(set(combined_list))
    cubed_list = [value ** 3 for value in unique_list]
    return cubed_list


list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 3, 6, 7, 8, 9]

result = unique_and_cubed_list (list_1, list_2)

print(result)
