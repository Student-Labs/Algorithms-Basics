def find_prime_numbers(range_start, range_end):
    result = []
    for number in range(range_start, range_end + 1):
        if number == 2:
            result.append(number)
        for element in range(2, number):
            if number % element >= 1:
                if element == number - 1:
                    result.append(number)
            else:
                break
    return result


def sum(result):
    sum = 0
    for number in result:
        sum = sum + number
    return sum


range_start = int(input("Input start number:\n"))
range_end = int(input("Input end number:\n"))
result = find_prime_numbers(range_start, range_end)
sum_of_prime_numbers = sum(result)
print(result)
print(sum_of_prime_numbers)
