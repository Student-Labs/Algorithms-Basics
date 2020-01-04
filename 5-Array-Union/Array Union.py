def array_union(first, second):
    result = []
    try:
        if first != ['']:
            first = contains_2(first)
            for number in first:
                bull = contains(number, second)
                if bull == True:
                    delete_element(first, number)
                elif bull == False:
                    number = int(number)
                    result.append(number)
        if second != ['']:
            second = contains_2(second)
            for number in second:
                number = int(number)
                result.append(number)
        return result
    except ValueError:
        if number in first:
            first = delete_element(first, number)
        elif number in second:
            second = delete_element(second, number)
        result = array_union(first,second)
        return result


def delete_element(array, element):
    array.remove(element)
    return array


def contains(number, array):
    if number in array:
        return True
    else:
        return False


def contains_2(array):
    new_array = []
    for element in array:
        bull = contains(element, new_array)
        if bull == False:
            new_array.append(element)
    return new_array


result = []
while result == []:
    first = (input("Enter numbers1:")).split(",")
    second = (input("Enter numbers2:")).split(",")
    result = array_union(first, second)
print(sorted(result))
