def find_prime_numbers(range_start, range_end):
    result = []
    numbers = [True] * range_end
    numbers[1] = numbers[0] = False
    for number in range(2, range_end):
        if numbers[number]:
            for element in range(2 * number, range_end, number):
                numbers[element] = False
    for number in range(range_end):
        if numbers[number]:
            if number >= range_start:
                result.append(number)
    return result


range_start = int(input("Input start number:\n"))
range_end = int(input("Input end number:\n"))
result = find_prime_numbers(range_start, range_end)
print(result)
