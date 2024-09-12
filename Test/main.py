# Write a function for each subtask
# Task 1.
# Write a Python program to create a list containing the following
# numbers: 10, 20, 30, 40, 50.
#               sub-task1: Print the list.

# Task 2.
# Given the list
#       numbers = [10, 20, 30, 40, 50],
#
#       write a Python program to:
#       sub-task2: Print the first element of the list.
#       sub-task4: Print the third element of the list.
#       sub-task5: Change the second element of the list to 25 and print the updated list.
#       sub-task6: Insert the number 15 at the second position in the list

# Task 3.
# Given the list
#       matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
#
#       write a Python program to:
#       sub-task7: Print the second element of the second list.
#       sub-task8: Print all the elements from the first, third and last list.

# Task 4.
# Write a Python program to create a dictionary with the following key-value pairs
#       sub-task9: Print the dictionary
# Given the following dictionary
#       person = {"name": "Alice", "age": 25, "city": "New York"},
#
#       write a Python program to:
#       sub-task9: Print the value associated with the key "name".
#       sub-task10: Print the value associated with the key "age".
#       sub-task11: Print the value of the "city" key using the get() method.

# Task 5.
# Write a Python program that takes a list of fruits:
#       fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]

#       sub-task12: Create a dictionary that counts the number of occurrences of each fruit, resulting in:
#           {"apple": 3, "banana": 2, "cherry": 1}

def number_list(list):
    """
    Description: O functie care creaza o lista de numere si o printeaza
    :return:
    """
    print(list_of_numbers)

def print_first_element(list):
    """
    Description: Printeaza primul element dintr-o lista
    :param list:
    :return:
    """
    print(list[0])

def print_third_element(list):
    """
    Description: Printeaza al treilea element dintr-o lista
    :param list:
    :return:
    """
    print(list[2])

def change_element_from_list(list):
    """
    Description: Change the second element of the list to 25 and print the updated list.
    :param list:
    :return:
    """
    list[1] = 25
    print(list)

def insert_number_in_list(list):
    """
    Description: Insert the number 15 at the second position in the list
    :return:
    """
    list.insert(1, 15)
    print(list)

def print_element_from_list_in_list():
    """
    Description: Print the second element of the second list
    :return:
    """
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    element=matrix[1]
    print(element[1])

def print_elements():
    """
    Description: matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    :return:
    """
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print(matrix[0], matrix[2], matrix[-1])

def print_dict(my_dict):
    """
    Description: Printeaza dictionarul
    :param my_dict:
    :return:
    """
    print(my_dict)
def print_value_from_dict():
    """
    Description: Print the value associated with the key "name"
    :return:
    """
    person = {"name": "Alice", "age": 25, "city": "New York"}
    print(person.get("name"))
    print(person.get("age"))
    print(person.get("city"))

if __name__ == "__main__":
    print("Welcome to the first test of the course!")
    print("------TASK1------")
    list_of_numbers = [10, 20, 30, 40, 50]
    print(number_list(list_of_numbers))
    print("\n")
    print("------TASK2------")
    print("------subtask1------")
    print_first_element(list_of_numbers)
    print("------subtask2------")
    print_third_element(list_of_numbers)
    print("------subtask3------")
    change_element_from_list(list_of_numbers)
    print("------subtask4------")
    insert_number_in_list(list_of_numbers)
    print("\n")
    print("------TASK3------")
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print("------subtask1------")
    print_element_from_list_in_list()
    print("------subtask2------")
    print_elements()
    print("\n")
    print("------TASK4------")
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    print("------subtask1------")
    print_dict(person)
    print("------subtask2-3-4-----")
    print_value_from_dict()
