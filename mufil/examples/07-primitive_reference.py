# Primitive Data Type Example (Immutable Type)
academy_name = "Adzyn Academy"  # String is a primitive data type (immutable)

def change_primitive_value(academy_name):
    # Iterate through the string and replace 'A' with 'a'
    for char in academy_name:
        if char == "A":
            # Strings are immutable, so this creates a new string rather than modifying the original
            academy_name = academy_name.replace(char, "a")
    return academy_name

print("Modified academy_name (Primitive Data Type):", change_primitive_value(academy_name))  # Outputs modified string
print("Original academy_name (Primitive Data Type):", academy_name)  # Original string remains unchanged

# Reference Data Type Example (Mutable Type)
tutor_name = ['M', 'U', 'F', 'I', 'L', ' ', 'R', 'A', 'H', 'M', 'A', 'N', ' ', 'A']  # List is a reference data type (mutable)

def change_reference_value(tutor_name):
    # Iterate through the list and replace 'M' with 'm'
    for i in range(len(tutor_name)):
        if tutor_name[i] == "M":
            # Lists are mutable, so the original list is modified in place
            tutor_name[i] = "m"
    return tutor_name

print("Modified full_name (Reference Data Type):", change_reference_value(tutor_name))  # Outputs modified list
print("Original full_name (Reference Data Type):", tutor_name)  # Original list is modified
