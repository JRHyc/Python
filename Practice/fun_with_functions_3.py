def multiply(arr,num):
  for x in range(len(arr)):
      arr[x] *= num
  return arr

newer_list = []
user_list = ([2,4,5],3)

multiplied_list = multiply(user_list[0], user_list[1])  
def layered_multiples(arr):
    
    for x in range(len(multiplied_list)):
        new_arr = []
        
        for i in range(multiplied_list[x]):
            print 1
            new_arr.append(1)
        newer_list.append(new_arr)
    
    print newer_list

layered_multiples(user_list)

