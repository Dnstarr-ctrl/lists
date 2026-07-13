def multiply_tuple(numbers):
    product = 1
    for x in numbers:
        product *= x
    return product


tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

print(f"Product of tup1: {multiply_tuple(tup1)}")
print(f"Product of tup2: {multiply_tuple(tup2)}")

