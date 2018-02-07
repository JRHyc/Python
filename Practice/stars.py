# ****
# ******
# *
# ***
# *****
# *******
# *************************

z = [4, 6, 1, 3, 5, 7, 25]
w = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(arr):
    
    for i in range(len(arr)):
        string_sum = ""
        for j in range(arr[i]):
            string_sum = string_sum + "*"
        print string_sum
draw_stars(z)