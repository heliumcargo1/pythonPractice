# The yeild function remembers the value & state of the iterate and returns it



def even_generator(num):
    for i in range(2,num+1,2):
        yield i


for j in even_generator(10):
    print(j)