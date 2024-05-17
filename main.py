def check_prime_number(num:int):
    if num <=2:
        print('number must be more than 2')
    if num >2:
        for i in range(2, (num-1)):
            if(num % i) == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
check_prime_number(11)