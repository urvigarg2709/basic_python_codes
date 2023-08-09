# Square each element of a list using list comprehension
original_list = [1, 2, 3, 4, 5]
squared_list = [x ** 2 for x in original_list]
print("Original List:", original_list)
print("Squared List:", squared_list)

# Square the values of a dictionary using dictionary comprehension
original_dict = {'a': 2, 'b': 3, 'c': 4}
squared_dict = {key: value ** 2 for key, value in original_dict.items()}
print("\nOriginal Dictionary:", original_dict)
print("Squared Dictionary:", squared_dict)
