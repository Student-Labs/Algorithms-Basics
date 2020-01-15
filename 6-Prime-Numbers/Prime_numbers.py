def find_prime_numbers(range_start, range_end):
    result = []
    for number in range(range_start, range_end):
        for element in range(2, number):
            if number % element >= 1:
                if element == number-1:
                    result.append(number)
            else:
                break
    return result


range_start = int(input("Input start number:\n"))
range_end = int(input("Input end number:\n"))
result = find_prime_numbers(range_start, range_end)
print(result)
