import cmath
import math
print("better version of calculator, choose a module")

choose_mod = input("1: complex numbers \n2: logarithms \n3: explain the module "  )

def module_1():
    while True:
        try:
            print("complex numbers")
            choose_operator = input("+ - * / or x to end: ")
            if choose_operator.lower() == "x":
                return

            c_num1 = complex(input("first number:  (a + bj)"))
            c_num2 = complex(input("second:  "))


            if choose_operator.lower() == "+":
                sum = c_num1 + c_num2
                print(sum)
            elif choose_operator.lower() == "-":
                sum = c_num1 - c_num2
                print(sum)
            elif choose_operator.lower() == "*":
                sum = c_num1 * c_num2
                print(sum)
            elif choose_operator.lower() == "/":
                sum = c_num1 / c_num2
                print(sum)

        except ValueError:
            print()

def module_2():
    while True:
        try:
            print("logarithms")
            base = float(input("base: "))
            number = float(input("number: "))

            result = math.log(number, base)
            print(result)
            cancel_mod_2 = input("continue with enter or x to kill: ")
            if cancel_mod_2.lower() == "x":
                return

        except ValueError:
            print()

def module_3():
    print("explanation")
    while True:
        exp_1 = "complex numbers: These exist to solve equations like x^2 + 1 = 0. Here, x would be the square root of -1, which is i (imaginary unit). The square root of -2 would be 1.41... i on the imaginary axis. Every number, including all natural numbers, are also complex numbers. A complex number c is composed as follows: c = a + b * i. a is the real part and b is the imaginary part. Example: square root of -25 + 4 = 5i + 4"
        exp_2 = "logarithms: logarithms are the opposite of exponentiation. For example, 5^2 = 25. log5 (25) = 2. So the question is 'what power of the base (5) gives the number (25)?'"
        which_exp = input("number of the module you want explained or 'x' to exit: ")
        if which_exp.lower() == "1":
            print(exp_1)
        if which_exp.lower() == "2":
            print(exp_2)
        if which_exp.lower() == "x":
            return

if choose_mod == "1":
    module_1()
if choose_mod == "2":
    module_2()
if choose_mod == "3":
    module_3()
while True:
    end_any = input("number of your module or 'x' to kill: ")

    if end_any.lower() == "1":
        module_1()
    if end_any.lower() == "2":
        module_2()
    if end_any.lower() == "3":
        module_3()
    if end_any.lower() == "x":
        break
           
