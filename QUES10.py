# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# prime_numbers = [num for num in range(2, 20) if is_prime(num)]6
# print("Prime numbers less than 20:", prime_numbers)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# num = int(input("Enter a number: "))
# fact = factorial(num)
# print("Factorial of", num, "is", fact)
def get_unique_sorted_words(file_path):
    unique_words = set()
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            unique_words.update(words)
    return sorted(unique_words)

file_path = input("Enter the path to the text file: ")
unique_words = get_unique_sorted_words(file_path)
print("Unique words in alphabetical order:")
for word in unique_words:
    print(word)

