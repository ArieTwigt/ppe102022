## Selecting elements from lists

#%%
flower_list = ['rose', 'gerbera', 'lily', 'dandilion']
#                  0       1         2         3
#                -4       -3        -2        -1
#%%
flower_list[0]
# %%
flower_list[2]
# %%
flower_list[-1]
# %% getting a slice from a list
flower_list[0:2]
# %% slices from
flower_list[1:]
# %%


## Modifying lists
#%%
flower_list[2] = 'tulip'
# %%
flower_list = ['rose', 'gerbera', 'lily', 'dandilion']
# %%
flower_list.append('tulip')
# %%
flower_list
# %%
name_list = []
# %%
name_list.append("arie") # changing the state of the 'name_list'
# %%
name_list.remove("arie")
name_list

## 
# %%
numbers_list = [5,1,2,4,4,5,5,11,5]

#%%
list(set(numbers_list))
# %%
numbers_list.index(5)


# %%
print(numbers_list)
numbers_list.sort() # changing the state of the list
print(numbers_list)

# %%
my_mixed_list = [4, 5, 'rose', 6, 'tulip']
my_mixed_list

# %%
my_mixed_list.append(numbers_list) # add the list "into" the my_mixed_list

# %%
my_mixed_list + numbers_list # concatenat/combine the two lists

# %%


