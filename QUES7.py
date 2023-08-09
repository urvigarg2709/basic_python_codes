# Create a tuple with different data types
my_tuple = (1, "hello", 3.14, False)

# Print the tuple
print("Tuple:", my_tuple)

# Create a dictionary with tuple keys
my_dictionary = {
    (1, 2): "Value 1",
    ("apple", "banana"): "Value 2",
    (True, False): "Value 3"
}

# Access elements in the dictionary using tuple keys
key_to_access = ("apple", "banana")
if key_to_access in my_dictionary:
    print(f"Value for key {key_to_access}: {my_dictionary[key_to_access]}")
else:
    print("Key not found in the dictionary.")
