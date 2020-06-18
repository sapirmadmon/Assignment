#Roei Berko - 205680747, Sapir Madmon - 209010230


#1st question - get sum of list
def sum_list(lst):
    total_value = 0
    if len(lst) == 0:
        return total_value
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            total_value += lst[i][j]
    return total_value


#2nd question - part A, reverse string
def reverse_string(str):
    if len(str) == 1:
        return str
    return str[::-1]


#2nd question - part B, reverse list
def reverse_list(lst):
    lst = [x[::-1] for x in lst[::-1]]
    return lst


#2nd question - part C, reverse tuple
def reverse_tuple(tpl):
    return tpl[::-1]


#3rd question - part A, sort tuple of sets
def sort_sets(tpl):
    list_of_nums = []
    list_of_chars = []
    sorted_list = []
    for i in range(len(tpl)):
        temp = list(tpl[i])
        for j in range(len(temp)):
            if isinstance(temp[j], int) or isinstance(temp[j], float):
                 list_of_nums.append(temp[j])
            else:
                list_of_chars.append(temp[j])

        sorted_list = sorted(list_of_chars) + sorted(list_of_nums)
    return sorted_list


#3rd question - part B, sort tuple of sets and return dictionary
def sort_dic(tpl):
    list_of_nums = []
    list_of_chars = []
    dict_of_words = {}
    for i in range(len(tpl)):
        temp = list(tpl[i])
        for j in range(len(temp)):
            if isinstance(temp[j], int) or isinstance(temp[j], float):
                 list_of_nums.append(temp[j])
            else:
                list_of_chars.append(temp[j])

        sorted_list = sorted(list_of_chars) + sorted(list_of_nums)
        dict_of_words = {i: sorted_list[i] for i in range(len(sorted_list))}
    return dict_of_words


#4th question - part A, same code without IF
def user_input1():
    x = int(input("Please enter a number:"))
    y = [9, 6][x > 10]
    return y


#4th question - part B, same code with one line IF
def user_input2():
    x = int(input("Please enter a number:"))
    y = 6 if x > 10 else 9
    return y


#5th question - part A, print range of input numbers only FOR loop
def print_range_with_for():
    start = int(input("Enter the start of range:"))
    end = int(input("Enter the end of range:"))
    for num in range(end, start, -1):
        even = int(num % 2 == 0)
        for i in range(even):
            print(num, end=" ")
    print("\n")
    for num in range(start, end + 1, 1):
        even = int(num % 2 == 0)
        for i in range(even):
            print(num, end=" ")


#5th question - part B, print range of input numbers only WHILE loop
def print_range_with_while():
    start = int(input("Enter the start of range:"))
    end = int(input("Enter the end of range:"))
    x = start
    y = end
    while y >= x:
        while y % 2 == 0:
            print(y, end=" ")
            y -= 1
            break
        y -= 1

    x = start
    y = end
    print("\n")
    while x <= y:
        while x % 2 == 0:
            print(x, end=" ")
            x += 1
            break
        x += 1



#5th question - part C: yes we can do that only with if statement using recursion!


#start tests

def test_sum_list():
    lst = [[3, 2], [1], [4, 12]]
    print("the sum is: ", sum_list(lst))


def test_reverse_string():
    s = "Hello World"
    print("\n")
    print("reverse string: ", reverse_string(s))


def test_reverse_list():
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("\n")
    print("reverse list: ", reverse_list(lst))


def test_reverse_tuple():
    tpl = ("apple", "banana", "cherry")
    print("\n")
    print("reverse tuple is: ", reverse_tuple(tpl))


def test_sort_sets():
    tuple_of_sets = ({1.7, 'a', 3}, {10, 11, 'b'}, {6.6, 7.7, 'c'})
    print("\n")
    print("the sorted set is: ", sort_sets(tuple_of_sets))


def test_sort_dict():
    tuple_of_sets = ({1.7, 'a', 3}, {10, 11, 'b'}, {6.6, 7.7, 'c'})
    print("\n")
    print("the sorted dict is: ", sort_dic(tuple_of_sets))


def test_user_input1():
    print("\n")
    print(user_input1())


def test_user_input2():
    print("\n")
    print(user_input2())


def test_print_range_with_for():
    print("\nrange with FOR")
    print_range_with_for()


def test_print_range_with_while():
    print("\nrange with WHILE")
    print_range_with_while()


if __name__ == "__main__":#unit test
    test_sum_list()
    test_reverse_string()
    test_reverse_tuple()
    test_sort_sets()
    test_sort_dict()
    test_user_input1()
    test_user_input2()
    test_print_range_with_for()
    test_print_range_with_while()
