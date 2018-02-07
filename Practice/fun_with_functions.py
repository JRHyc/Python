# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.

def odd_even():
    for x in range(1, 2001):
      if x % 2 == 0:
        print "The number is {} and its even".format(x)
      else:
        print "The number is {} and its odd".format(x)

odd_even()
