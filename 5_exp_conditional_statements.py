#%%
numbers_list = [1,11,56]

#%%
if len(numbers_list) > 0 or len(numbers_list) != 3:
    print("This list is not empty")
elif len(numbers_list) == 3:
    print("This list has 3 items")
else:
    print("This list is empty")

print("This is the rest of the code")

# %%
numbers_list = [1,11,56]


#%%
number = 20

if number in numbers_list:
    print(f"{number} is in the list")
else:
    print(f"{number} is not in the list")
    numbers_list.append(number)
    print(f"{number} is added to the list")
    print(f"The list is now: {numbers_list}")


print("\nThis is the rest of the code")

# %%
numbers_list = [1,10,56]
    
if (len(numbers_list) != 0 and 11 in numbers_list) or 56 in numbers_list:
    print("Het klopt")
    
# %%
