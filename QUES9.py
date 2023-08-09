def relu(x):
    if x >= 0:
        return x
    else:
        return 0

# Test the function
input_value = float(input("Enter a number: "))
result = relu(input_value)
print("ReLU result:", result)
