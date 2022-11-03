def checkPrimeNo(num):
    # checking for prime numbers from 2 to range
    for i in range(2,num):
        if num % i == 0:
            print('The number is not prime')
            break
        else:
            print('The number is prime ')
            