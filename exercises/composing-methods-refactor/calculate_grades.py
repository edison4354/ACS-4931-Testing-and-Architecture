"""This module provides access to the mathematical functions defined by the C standard"""
import math


def find_mean(all_grades):
    """Return the mean of grades"""
    total = 0
    for grade in all_grades:
        total += grade
    return total / len(all_grades)


def standard_deviation(all_grades, mean):
    """Return the standard deviation of grades"""
    sum_of_sqrs = 0
    for grade in all_grades:
        sum_of_sqrs += (grade - mean) ** 2
    return math.sqrt(sum_of_sqrs / len(all_grades))


def print_stat():
    """Prints out the mean and standard deviation"""
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))

    # Calculates mean and stand deciation
    mean = find_mean(grade_list)
    s_deviation = standard_deviation(grade_list, mean)

    # prints out the mean and standard deviation in a nice format
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(s_deviation, 3))
    print('****** END ******')


print_stat()
