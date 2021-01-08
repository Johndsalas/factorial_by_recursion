'''
Contains function that will get the factorial of a number using recursion
'''

def get_factorial(number):
    '''
    Gets the factorial of a number using recursion
    '''


    # base case if number is zero return one
    if number == 0:

        number = 1

        return number

    # if this is not the base case
    # get the number times the get_factorial of the number minus one
    return number * get_factorial(number-1)
