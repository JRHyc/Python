
exOne = ['magical unicorns',19,'hello',98.98,'world',7, 9]
exTwo = [2,3,1,7,4,12]
exThree = ['magical','unicorns']

def checkType(a_list):
    listLength = len(a_list)
    stringSum = ""
    numSum = 0
    temp_type = ""

    for x in range(0, listLength):
        if isinstance(a_list[x], str):
            temp_type = "All Strings"
        elif isinstance(a_list[x], int):
            temp_type = "All integers"
        else:
            temp_type = "Mixed"
            break
    for x in range(0, listLength):
        if isinstance(a_list[x], str):
            stringSum += a_list[x] + " " 
        elif isinstance(a_list[x], int):
            numSum += a_list[x]

    print ("The list is {}".format(temp_type))
    print ("The total sum of the list is {}".format(numSum))
    print ("The strings of the list equal: {}".format(stringSum))
checkType(exThree)