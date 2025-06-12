upper_limit = 20

for a in range(2, upper_limit):

    # This checks if a is a prime number
    is_prime = True

    for i in range(2, int(a/2)+1):
        if a % i == 0:
            is_prime = False
            break
        
    if is_prime == True:   
        print (a)


    
















    
