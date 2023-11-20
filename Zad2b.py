
# Loop:
def double_elements1(list):
    for i in range(len(list)):
        list[i] *= 2
    return list


list1 = [1, 2, 3, 4, 5]
output1 = double_elements1(list1)
print("Loop:", output1)

# List comprehension:


def double_elements2(list):
    return [x * 2 for x in list]


list2 = [1, 2, 3, 4, 5]
output2 = double_elements2(list2)
print("List comprehension:", output2)
