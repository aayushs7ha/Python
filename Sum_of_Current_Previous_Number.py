# Intialize Previous Number
previous_num = 0 

# Define Range
for i in range(1,11):
    # Sum = of previous number + start of range
    sum = previous_num + i
    # Print previous number, i -> the current number, sum of them both
    print("previous_number",previous_num,i,"sum",sum)
    # previous number after sum; becomes the current number 
    previous_num = i 