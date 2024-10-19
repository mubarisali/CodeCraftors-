name = "ajay joy"

def change_name(name):
    for char in name:
        if char.islower():
            name = name.replace(char, char.upper())
    return name
    
print(f"modified name : {change_name(name)}")
print(f"Original name : {name}") 

# Strings are immutable ,it creates a new string rather than modifying the original string.

name_list = ['a', 'j', 'a', 'y', 'j', 'o', 'y']
print(f"Original name_list before modifying: {name_list}") 

def change_name_list(name):
    for i in range(len(name)):
        if name[i].islower():
            name[i] = name[i].upper()  
    return name
            
modified_name = change_name_list(name_list)

print(f"Modified name_list: {modified_name}")
print(f"Original name_list after modifying: {name_list}")

# List are mutable ,so the changes in original list will reflect the same list itself.