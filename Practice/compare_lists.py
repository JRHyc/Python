list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']
list_length = len(list_one)
final_answer = ""

def compare(one, two):
    
    for x in range(0, list_length):
        if(len(one) != len(two)):
            final_answer = "The two lists are not the same length"
            break
        if(one[x] != two[x]):
            final_answer = "The two lists are not the same"
            break
        else:
            final_answer = "The lists are the same"

    print final_answer
compare(list_one, list_two)