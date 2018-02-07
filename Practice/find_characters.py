
# new_list = ['hello','world']

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

def find_words(user_list, character):
    list_length = len(user_list)
    for x in range(0, list_length):
        if character in user_list[x]:
            new_list.append(user_list[x])
            
    print new_list
find_words(word_list, char)