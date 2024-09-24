teas = ["black","green","masala","lemon"]

# print(teas[1:2])
teas[1:2]= ["lemon"] #here we are replacing the green with lemon and value should always be in list[], we shouldnt give like this "lemon"
#print(teas)             #because it will treat like an list and the output would be like 'l', 'e', 'm', 'o', 'n'

teas[1:2] = [] #this method is called "Delete nothing", in the list it will take the item from 1 till 2 and it will replace with nothing/ empty list
print(teas)