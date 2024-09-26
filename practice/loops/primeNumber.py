number = 18
isPrime = True

# the prime number are those numbers divisible by itself or one 

if number >1:
    for i in range(2,number): #here we take number instead of number+1 because if number % number = 0 then it will return true even tho the number is not a prime
        print("loop i",i)
        if (number % i) == 0:
            print("if i",i)
            isPrime = False
            print("the number", number, "is prime = ",isPrime )
            break

if isPrime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")