# Create a set with different data types
my_set = {1, "hello", 3.14, True}

# Check for an element in the set
element_to_check = "hello"
if element_to_check in my_set:
    print(f"'{element_to_check}' is present in the set.")
else:
    print(f"'{element_to_check}' is not present in the set.")

# Add elements to the set
my_set.add(42)
my_set.add("world")
print("\nSet after adding elements:", my_set)

# Remove elements from the set
my_set.discard(3.14)
my_set.remove(True)
print("Set after removing elements:", my_set)
