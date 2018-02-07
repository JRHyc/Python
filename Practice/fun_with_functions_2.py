# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
# and returns a list where each value has been multiplied by 5.

# The function should multiply each value in the list by the second argument. For example, let's say:
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

a = [2,4,10,16]
print multiply(a,5)
