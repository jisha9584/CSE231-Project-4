###########################################################
#  Computer Project #4
#
#  Print MENU
#    define functions
#       1. factorial
#       2. e
#       3. pi
#       4. sinh(x)
#    define main
#       pull all 4 functions and define calculate, math and their difference 
#       use string.txt for formating 
#       write code for all the options on menu
#    print end statement: Thank you for playing
###########################################################

import math
EPSILON = 0.0000001 

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''
def factorial(N): 
    ''' 
    calculate the factorial of the input (N)
    N: the value to be processed (str): 3 arguments- for 0 return 1, for not N<0 and digit return none and calculate the factorial
    Returns: the factorial of N
    '''
    N_int= int(N)
    if N_int == 0:
        return 1
    elif N_int < 0:
        return None
    factorial=1
    for i in range(1, N_int+1):
        factorial*= i
    return factorial
 
def e(): 
    ''' 
    calculate the e value
    value: No argument 
    return: the rounded value of e from the funtion 
    ''' 
    N_flt= 0
    e_sum_flt= 1
    add_flt= 0
    while math.fabs(e_sum_flt)>=EPSILON: #value should be greater than EPSILON
        add_flt=e_sum_flt+add_flt
        N_flt+=1
        e_sum_flt = 1/math.factorial(N_flt)
    return round(add_flt,10) #round to 10

def pi():
    ''' 
    calculate the pi value
    value: No argument 
    return: the rounded value of pi from the funtion 
    ''' 
    pi_flt= 0
    pi_sum_flt= 0
    pi_terminal_flt= 1
    while abs(pi_terminal_flt)>= EPSILON: #value should be greater than EPSILON
        pi_flt+= pi_terminal_flt
        pi_sum_flt+=1
        pi_terminal_flt = ((-1)**pi_sum_flt)/(2*pi_sum_flt+1)
    return round(pi_flt*4, 10) #round to 10

def sinh(x): 
    ''' 
    calculate the sinh of the input (x)
    X: the value to be processed (str) *convert to flt* 
    Returns: the sinh of x
    ''' 
    sin_total= 0
    n=0
    try:
        x = float(x)
        c = (x**(2*n+1))/(math.factorial(2*n+1))
        while math.fabs(c) >= EPSILON: #value should be greater than EPSILON
            sin_total+=c
            n+=1
            c = (x**(2*n+1))/(math.factorial(2*n+1))
        return round(sin_total, 10) #round to 10
    except ValueError:
        return None

def main(): 
    print(MENU) 
    option = input("\nChoose an option: ")
    option1 = option.isalpha() #to make sure it is in the right input 
    while option1 == True:
        if option == "F" or option == "f": #for capital and small letters
            print("\nFactorial")
            N= input("Input non-negative integer N: ") 
            try: 
                N_int= int(N)
                if N_int>0: #for the -2 case 
                    print("\nCalculated:", factorial(N_int))
                    print("Math:", math.factorial(N_int))
                    print("Diff:", abs(factorial(N_int) - math.factorial(N_int)))
                    option = input("\nChoose an option: ")
                else:
                    print("\nInvalid N.")
                    option = input("\nChoose an option: ")
            except ValueError: 
                print("\nInvalid N.")
                option = input("\nChoose an option: ")
            except TypeError:
                print("\nInvalid N.")
                option = input("\nChoose an option: ")
        elif option == "E" or option == "e": #for capital and small letters
            print("\ne")
            print("Calculated:", e())
            print("Math:", round(math.e, 10)) #round to 10
            print("Diff: {:.10f}".format(abs(e()-math.e)))
            option = input("\nChoose an option: ")
        elif option == "P" or option == "p": #for capital and small letters
            print("\npi")
            print("Calculated:", pi())
            print("Math:", round(math.pi, 10))
            print("Diff: {:.10f}".format(abs(pi()- math.pi)))
            option = input("\nChoose an option: ")
        elif option == "S" or option == "s": #for capital and small letters
            print("\nsinh")
            try:
                x_flt= float(input("X in radians: "))
                print("\nCalculated:", sinh(x_flt))
                print("Math:", round(math.sinh(x_flt), 10)) #round to 10
                print("Diff: {:.10f}".format(math.fabs(sinh(x_flt)- math.sinh(x_flt))))
                option = input("\nChoose an option: ")
            except ValueError:
                print("\nInvalid X.")
                option = input("\nChoose an option: ")
        elif option == "M" or option == "m": #for capital and small letters #test1
            print(MENU)
            option = input("\nChoose an option: ")
        elif option == "X" or option == "x": #for capital and small letters
            break  
        else:
            option= option.upper()
            print("\nInvalid option:", option)
            print (MENU)
            option = input("\nChoose an option: ")
    print("\nThank you for playing.")

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()
