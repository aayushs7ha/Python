    # Calculate the multiplication if sum of two numbers is less than 1000 and 
    # sum of two numbers if the sum of two numbers is more than 1000
    
def sumProd(num1,num2):
        result = num1*num2
        if result < 1000:
            print("Result",result)
        else:
            result = num1 + num2

sumProd(10,30)