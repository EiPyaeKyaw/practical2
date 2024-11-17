def display_main_menu():
    print("Enter some numbers separated by commas (e.g, 5, 67, 32)")

def get_user_input():
    user_input = input("Enter some numbers : ").split(",")
    float_list = []
    for list in user_input:
        float_list.append(float(list))
    print(type(user_input))
    return float_list

def calc_average(list):
    avg = sum(list)/len(list)
    print("calc_average = " + str(avg))
    return 

def find_min_max(list):
    print(max(list))
    print(min(list))

def sort_temperature(list):
    print(sorted(list))

def calc_median_temperature():
    print("calc_median_temperature")

get_user_input()
list = get_user_input()
calc_average(list)
find_min_max(list)
sort_temperature(list)