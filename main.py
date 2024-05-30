import cmath
import math
print("better version of calculator, choose a module")

choose_mod = input("1: komplexe zahlen \n2: logarithmen lösen \n3: erklärung für das jeweilige modul "  )

def module_1():
    while True:
        try:
            print("komplexe zahlen")
            choose_operator = input("+ - * / oder x zum beenden: ")
            if choose_operator.lower() == "x":
                return

            c_num1 = complex(input("erset zahl (a + bj)"))
            c_num2 = complex(input("zweite: "))


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
            print("logarithmen")
            base = float(input("basis: "))
            zahl = float(input("zahl: "))

            result = math.log(zahl, base)
            print(result)
            cancel_mod_2 = input("mit enter weitermachen oder 'x' zu, beenden drücken: ")
            if cancel_mod_2.lower() == "x":
                return

        except ValueError:
            print()

def module_3():
    print("erklärung für das jeweilige modul")
    while True:
        exp_1 = "komplexe zahlen: Diese sind da, um z.B die Gleichung x ^2 + 1 = 0 zu lösen. hier wäre x = die wurzel aus -1, das ist ein mal i (imaginäre einheit) die wurzel aus -2 wäre auf der imaginären achse 1,41... i. jede zahl, also alle natürlichen zahlen etc sind gleichzeitig auch komplexe zahlen. Eine komplexe zahl c setzt sich so zusammen : c = a + b * i. a gleich realteil und b der imaginärteil. beispiel: wurzel -25 + 4 = 5i + 4"
        exp_2 = "logarithmen: logarithmieren ist das gegenteil zum potenzieren. z.B 5^ 2 = 25. log5 (25) = 2. also stellt sich die frage 'was hoch die basis (5) ergibt die zahl (25)? ' "
        which_exp = input("nummer des moduls das du erklärt haben möchtest oder 'x' zum beenden: ")
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
    end_any = input("nummer deines moduls oder 'x' zum beenden: ")

    if end_any.lower() == "1":
        module_1()
    if end_any.lower() == "2":
        module_2()
    if end_any.lower() == "3":
        module_3()
    if end_any.lower() == "x":
        break
           