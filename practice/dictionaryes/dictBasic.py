# Dict doesnt have any sequential order unlike lists
# it is define by key value pair



teas = {"masala":"spicy","ginger":"zesty","green":"mild"}

# print(teas)

# to extract one specific value of key pair 

# print(teas["ginger"])
# or
# print(teas.get("ginger")) 

# If there given key value isnt in the dict then it will return 'None'


# to Replace an value of an given key
teas["green"] = "Fresh"
# print(teas)


# # If we apply loop for dict it will return the keys 
# for i in teas:
#     print(i)

# # To print the values also 
# for i in teas:
#     print(i, teas[i])
# # or 
# for i,j in teas.items():
#     print(i,j)



# To Check if the Key is present in the dict

# if "green" in teas:
#     print("yes")
# else:
#     print("No")


# To add a entire new item in the dict

# teas["taj"] = "Sweet"
# print(teas)


# To pop an item from dict

# teas.pop("ginger") #it will pop the ginger key value pair from the dict
# print(teas)


# To remove the last added item from the dict
# teas.popitem()
# print(teas)


# To remove an item from the memory reference

# del teas["green"]
# print(teas)


# To use loop within dict

squared_num = {x:x**2 for x in range(5)}
print(squared_num) #output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# To remove all items from a dict

squared_num.clear()
print(squared_num)