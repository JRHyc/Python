# Start with a list like this one: . Sort your list first. 
 # Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. 
# [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
Final = []
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x = sorted(x)
# print x
NewBeg = x[:5]
NewEnd = x[5:]

Final.append(NewBeg)
Final = Final + NewEnd


print Final

# Print the first and last values in a list like this one:
# Now create a new list containing only the first and last values in the original list. Your code should work for any list.

# newList = []
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0]
# print x[-1]
# newList.append(x[0])
# newList.append(x[-1])
# print newList


# Print the min and max values in a list like this one: . Your code should work for any list.
# x = [2,54,-2,7,12,98]
# print max(x)
# print min(x)


# # Find and Replace
# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find("day")
# print words.replace("day", "month")



