def double_values(lst):
    return [x * 2 for x in lst]

print(double_values([1, 2, 3])) 

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  


def square_elements(lst):
    return [x ** 2 for x in lst]

print(square_elements([2, 3, 4])) 


def filter_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char in vowels])

print(filter_vowels("Hello World"))  


def filter_negative_numbers(lst):
    return [x for x in lst if x < 0]

print(filter_negative_numbers([-5, 3, 0, -2, 8])) 


def filter_positive_numbers(lst):
    return [x for x in lst if x > 0]

print(filter_positive_numbers([-5, 3, 0, -2, 8]))  


def square_and_multiply_by_10(n):
    return (n ** 2) * 10

print(square_and_multiply_by_10(4))  


def power(x, y):
    return x ** y

print(power(2, 3))  
