def prime_checker(num):
    # num = 13
    if num >1:
        for x in range(2, (num//2)+1):
            if (num % x ) == 0:
                print(f"{num} is not prime number")
                break
        else:
            print(f"{num} is a prime number") 
    else:
        print(f"{num} is not a prime number") 

prime_checker(11) 

