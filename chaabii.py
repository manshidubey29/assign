q1.def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

q2.def get_file_types(mapping, filenames):
    mapping_dict = {}

    # Create a dictionary from the extension-type mapping
    for item in mapping.split(';'):
        extension, file_type = item.split(',')
        mapping_dict[extension] = file_type

    result = {}

    # Determine the file type for each filename
    for filename in filenames:
        extension = filename.split('.')[-1]
        if extension in mapping_dict:
            result[filename] = mapping_dict[extension]
        else:
            result[filename] = 'unknown'

    return result

# Test the get_file_types function
mapping = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result = get_file_types(mapping, filenames)
print(result)


q3.def sort_list_of_dicts(lst, key):
    sorted_lst = sorted(lst, key=lambda x: x[key])
    return sorted_lst

# Test the sort_list_of_dicts function
lst1 = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
sorted_lst1 = sort_list_of_dicts(lst1, "fruit")
print(sorted_lst1)

lst2 = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
sorted_lst2 = sort_list_of_dicts(lst2, "color")
print(sorted_lst2)


q4.def switch_key_value(d):
    return {v: k for k, v in d.items()}

# Test the switch_key_value function
original_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
switched_dict = switch_key_value(original_dict)
print(switched_dict)



q5.def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements

# Test the compare_lists function
mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, non_common = compare_lists(mainstream, must_watch)
print(common)
print(non_common)


q6.def get_sublist(lst, start_index, end_index):
    sub_list = lst[start_index + 1:end_index:2]
    return sub_list

# Test the get_sublist function
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_sublist(lst, start_index, end_index)
print(result)


q7.from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

# Test the factorial function
number = 5
result = factorial(number)
print(result)


q8.A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
The final value of A0 is {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}. It is a dictionary created by zipping the keys ('a', 'b', 'c', 'd', 'e') with the values (1, 2, 3, 4, 5).

A1 = range(10)
The final value of A1 is range(0, 10). It is a range object representing numbers from 0 to 9.


A2 = sorted([i for i in A1 if i in A0])
The final value of A2 is [1, 2, 3, 4, 5]. It is a sorted list comprehension that filters out the numbers from A1 that exist as keys in A0.

A3 = sorted([A0[s] for s in A0])
The final value of A3 is [1, 2, 3, 4, 5]. It is a sorted list comprehension that retrieves the values from A0 based on the keys in A0.


A4 = [i for i in A1 if i in A3]
The final value of A4 is [1, 2, 3, 4, 5]. It is a list comprehension that filters out the numbers from A1 that exist in A3.


A5 = {i: i*i for i in A1}
The final value of A5 is {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}. It is a dictionary comprehension that creates a dictionary where the keys are the numbers from A1, and the values are the square of those numbers.


A6 = [[i, i*i] for i in A1]
The final value of A6 is [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]. It is a list comprehension that creates a list of lists where each inner list contains a number from A1 and its square.


from functools import reduce
A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
The final value of A7 is 21. It is obtained by applying the lambda function to reduce the list [10, 23, -45, 33] by performing the addition operation.


A8 = map(lambda x: x * 2, [1, 2, 3, 4])
The lambda function lambda x: x * 2 is applied to each element in the original list, resulting in each element being multiplied by 2. The final value of A8 will be a list containing the transformed elements.

Therefore, the final value of A8 will be [2, 4, 6, 8].

A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

The final value of A9 will be a list containing the elements from the original list that have a length greater than 3.

Therefore, the final value of A9 will be ['want', 'learn', 'python'].

q9.from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference between the dates
    date_difference = abs((to_date - from_date).days)

    # Check if the difference is less than the specified value
    if date_difference < difference:
        return True
    else:
        return False
q10.from datetime import datetime, timedelta

def calculate_previous_date(date, n):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the previous date by subtracting n days
    previous_date = date_obj - timedelta(days=n)

    # Format the previous date as a string in the desired format
    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str


q11.def f(x, l=None):
    if l is None:
        l = []
    for i in range(x):
        l.append(i * i)
    print(l)

f(2)
f(3, [3, 2, 1])
f(3)