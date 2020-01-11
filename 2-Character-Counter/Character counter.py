def symbol_counter(text):
    counter = 0
    array = []
    for symbol in text:
        for element in text:
            if symbol == element:
                counter += 1
        element = str(symbol) + '-' + str(counter)
        counter = 0
        array.append(element)
        array = delete_duplicated_elements(array)
    return array


def delete_duplicated_elements(array):
    new_array = []
    for element in array:
        if element not in new_array:
            new_array.append(element)
    return new_array


text = input("Write text and press enter:\n").lower()
text = text.split()
text = ''.join(text)
text = symbol_counter(text)
for element in text:
    print(element)
