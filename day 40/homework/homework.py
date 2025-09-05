def manual_find(s, char):
    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1

def manual_count(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count


word = "hello"
if "e" in word:
    print("'e' არის სიტყვაში")

numbers = [1, 2, 3, 4]
if 5 not in numbers:
    print("5 არ არის სიაში")