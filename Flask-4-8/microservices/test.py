import hafez

# List all available functions and attributes in the hafez package
attributes = dir(hafez)
print(attributes)

# Print the docstring of each attribute to understand their usage
for attr in attributes:
    if not attr.startswith('__'):
        print(f"{attr}: {getattr(hafez, attr).__doc__}")
