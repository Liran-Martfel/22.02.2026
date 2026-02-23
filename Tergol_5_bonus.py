list1 = [1, 3, 5, 6, 8, 9]
def remove_odd_even(list1, even):
    even_list = []
    odd_list = []
    for num in list1:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    if even == True:
        print(odd_list)
    else:
        print(even_list)


remove_odd_even(list1, False)