# Create a list with different data types
my_list = [1, "hello", 3.14, True, [5, 6]]

# Access elements of the list
print("List elements:")
print("Element 1:", my_list[0])
print("Element 2:", my_list[1])
print("Element 3:", my_list[2])
print("Element 4:", my_list[3])
print("Element 5:", my_list[4])

# Slicing the list
sliced_list = my_list[1:4]
print("\nSliced List:", sliced_list)

# Append elements to the list
my_list.append("new_element")
print("\nList after appending:", my_list)

# Remove elements from the list
my_list.remove(3.14)
print("List after removing:", my_list)
