def draw_stars_dos(arr):
    for index in new_array:
        string_sum = ""
        if type(index) == int:
            for j in range(arr[index]):
                print index
                string_sum = string_sum + "*"
        if type(index) == str:
            new_str = len(index) * index[:1]
            print new_str.lower()
new_array = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_dos(new_array)