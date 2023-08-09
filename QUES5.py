# Create a dictionary with different data types
my_dict = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "grades": [85, 92, 78],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}

# Access elements of the dictionary
print("Dictionary elements:")
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("Is Student:", my_dict["is_student"])
print("Grades:", my_dict["grades"])
print("Address:", my_dict["address"])

# Add elements to the dictionary
my_dict["phone"] = "555-1234"
my_dict["email"] = "john@example.com"
print("\nDictionary after adding elements:", my_dict)

# Remove elements from the dictionary
del my_dict["age"]
my_dict.pop("is_student")
print("Dictionary after removing elements:", my_dict)
