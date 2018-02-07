list_one = [1,2,3,4,5,6,7,8,9,10,11,12]
list_two = [1,2,3,4,5,6,7,8,9,10,11,12]

factor = 0
list_length = len(list_one)
def mulit_table(one, two):
    for x in range(0, list_length):
        factor = one[x] * two[x]
        print factor

mulit_table(list_one, list_two)