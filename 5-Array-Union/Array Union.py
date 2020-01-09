def array_union(first, second):
    result = []
    try:
        if first != ['']:
            first = contains(first)
            for number in first:
                if number in second:
                    first.remove(number)
                else:
                    number = int(number)
                    result.append(number)
        if second != ['']:
            second = contains(second)
            for number in second:
                number = int(number)
                result.append(number)
        return result
    except ValueError:
        if number in first:
            first.remove(number)
        elif number in second:
            second.remove(number)
        result = array_union(first, second)
        return result


def delete_duplicated_elements(array):
    new_array = []
    for element in array:
        if element not in new_array:
            new_array.append(element)
    return new_array


result = []
while result == []:
    first = (input("Enter numbers1:")).split(",")
    second = (input("Enter numbers2:")).split(",")
    result = array_union(first, second)
print(sorted(result))
