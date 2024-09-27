#the double ** takes the multiple key value pairs and assign  to the kwargs variable,
# the syntax should be always be in a loop  


def printKwargs(**kwargs):
    result = ""
    for key, value in kwargs.items():
          result +=  f"{key}: {value}\n"
    return result

k = printKwargs(name = "safi",lastname = "uddin")
print(k)

