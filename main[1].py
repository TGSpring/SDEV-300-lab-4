"""Tyler Spring
Lab 4, Part 1
This is the matrix game. It asks the user if they wish to play,
from there it asks the user to enter their phone
number and zipcode.
After that is asks the user to enter two different 3x3 matrixes.
It then asks the user to select what functions they
would like to do to the matrixes. When the user selects an option, it display the result,
"""

import re
import numpy as np


def add(oneM, twoM):
    """
The addition function takes two objects and creates two new array objects of this function.
It then adds the two and assigns it to a new variable that is the sum of the two.
It prints the new matrix out using nested for loops
    :rtype: object
    """
    print("Addition selected. Sum =  ")
    oneA = np.array(oneM)
    twoA = np.array(twoM)
    # Adding array objects together to get sum
    c = oneA + twoA
    for i in range(3):
        for k in range(3):
            print(c[i][k], end=" ")
        print()
    print("The transpose is:")
    tran = np.transpose(c)
    for i in range(3):
        for k in range(3):
            print(tran[i][k], end=" ")
        print()
    print("The row and column means are:\n"
          "Row: ", np.mean(c, axis=1), "\n"
                                       "Cols: ", np.mean(c, axis=0))


def minus(oneM, twoM):
    """
The subtraction function takes two objects and creates two new array objects of this function.
It then adds the two and assigns it to a new variable that is the sum of the two.
It prints the new matrix out using nested for loops
    :type oneM: object
    """
    print("Subtraction selected. Difference = ")
    oneA = np.array(oneM)
    twoA = np.array(twoM)
    # Subtracting array objects together to get difference
    c = oneA - twoA
    for i in range(3):
        for k in range(3):
            print(c[i][k], end=" ")
        print()
    print("The transpose is:")
    tran = np.transpose(c)
    for i in range(3):
        for k in range(3):
            print(tran[i][k], end=" ")
        print()
    print("The row and column means are:\n"
          "Row: ", np.mean(c, axis=1), "\n"
                                       "Cols: ", np.mean(c, axis=0))


def multi(oneM, twoM):
    """
The multiplication function takes two objects and creates two new matrix objects of this function.
It then multiplies the two and assigns it to a new variable that is the product of the two.
It prints the new matrix out using nested for loops
    :rtype: object
    """
    print("Multiplication selected. Product = ")
    oneA = np.matrix(oneM)
    twoA = np.matrix(twoM)
    # Multiplying matrix objects together to get product. Used matmul.
    # It worked good for getting the product,not for printing
    c = np.matmul(oneA, twoA)
    print(c)
    # Did the calculation here just to make it easier to print. Probably the wrong way but it worked.
    cp = oneA * twoA
    cp = np.array(cp)
    for i in range(3):
        for k in range(3):
            print(cp[i][k], end=" ")
        print()
    print("The transpose is:")
    tran = np.transpose(cp)
    for i in range(3):
        for k in range(3):
            print(tran[i][k], end=" ")
        print()
    print("The row and column means are:\n"
          "Row: ", np.mean(cp, axis=1), "\n"
                                        "Cols: ", np.mean(cp, axis=0))


def eMulti(oneM, twoM):
    """The element function takes two objects and creates two new array objects of this function.
It then multiplies the two and assigns it to a new variable that is the product of the two.
It prints the new matrix out using nested for loops

    :type oneM: object
    """
    print("Element by element multiplication selected. Product = ")
    oneA = np.array(oneM)
    twoA = np.array(twoM)
    # Multiplying array objects together to get product
    c = oneA * twoA
    for i in range(3):
        for k in range(3):
            print(c[i][k], end=" ")
        print()
    print("The transpose is:")
    tran = np.transpose(c)
    for i in range(3):
        for k in range(3):
            print(tran[i][k], end=" ")
        print()
    print("The row and column means are:\n"
          "Row: ", np.mean(c, axis=1), "\n"
                                       "Cols: ", np.mean(c, axis=0))


"""
This is the main driver of the class. It asks the user to either for either Y or N. After that it asks the user 
for their phone number and zip code. Both of which are validated. It then proceeds to have the user input their matrixes
and prompt them with the functions that are above.
"""
while True:
    # PLEASE ENTER ONLY Y OR N IN THEIR CORRECT CASE!
    print("Do you want to play the Matrix Game?")
    ans = input("Enter Y for yes, N for no.")
    if ans == 'N':
        print("*********** Thanks for playing Python Numpy ***************")
        break
    if ans == 'Y':
        print("Please enter phone number.")

        while True:
            phone = input()
            if re.match("\d{3}[-]\d{3}[-]\d{4}", phone):
                break

            print("Your phone number syntax is incorrect. ReEnter.")
        print("Enter your zipcode")
    while True:
        zipp = input()
        if re.match("\d{5}[-]\d{4}", zipp):
            break

        print("Your zip code syntax is wrong. ReEnter.")

    print("Enter 3 by 3 matrix")
    one = []
    for m in range(3):
        row = input().split()
        row = list(map(int, row))
        one.append(row)
    print("Matrix one is: ")
    for m in range(3):
        for x in range(3):
            print(one[m][x], end=" ")
        print()
    print("Enter second 3 by 3 matrix")
    two = []
    for q in range(3):
        row = input().split()
        row = list(map(int, row))
        two.append(row)
    print("Matrix two is:")
    for q in range(3):
        for z in range(3):
            print(two[q][z], end=" ")
        print()

    print("Which Matrix function would you like to do?\n"
          "a. Addition\n"
          "b. Subtraction\n"
          "c. Matrix Multiplication\n"
          "d. Element by element multiplication")
    choice = input()
    newM = np.zeros((3, 3))
    if choice == 'a':
        add(one, two)
    elif choice == 'b':
        minus(one, two)
    elif choice == 'c':
        multi(one, two)
    elif choice == 'd':
        eMulti(one, two)
    else:
        print("Invalid option. ReEnter.")
