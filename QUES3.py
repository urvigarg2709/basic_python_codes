# Sample strings
string1 = "hello"
string2 = "world"

# Print a string
print("String 1:", string1)
print("String 2:", string2)

# Concatenation of two strings
concatenated = string1 + " " + string2
print("Concatenated:", concatenated)

# Capitalize a string
capitalized = string1.capitalize()
print("Capitalized:", capitalized)

# Convert a string to uppercase
uppercase = string2.upper()
print("Uppercase:", uppercase)

# Right-justify a string
right_justified = string1.rjust(10)
print("Right-justified:", right_justified)

# Centre a string
centered = string2.center(15, "-")
print("Centered:", centered)

# Replace all instances of one substring with another
original_string = "I like cats, but cats are not as cute as dogs."
replaced_string = original_string.replace("cats", "dogs")
print("Replaced string:", replaced_string)

# Accessing substring from a given string
substring = original_string[7:11]
print("Substring:", substring)
