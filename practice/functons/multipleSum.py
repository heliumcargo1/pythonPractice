# Here the starting * takes all the paramerters and assign to the variable sides it 
# and the varible name should be args, not because it is mandetory but because it is recognised that way

def sum_all(*args):
    return sum(args)


print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,9090))