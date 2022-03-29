from week0.tree import tree
from week0.ship import ship
from week0.matrix import test_matrix
from week0.swap import test_swap
from week1.InfoDB import for_loop, while_loop, recursive_loop
from week1.factorial import tester
from week1.fibonacci import fibonacci
from week2.factorialClass import factorial
from week2.factors import factors, factorsTester
from week2.fiboCall import fiboCall
from week2.primes import primes, primesTester


main_menu = []

# Menu list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. "filename.py" will be run by exec(open("filename.py").read())
# 2. file.function references will be executed as file.function()

math_sub_menu = [
    ["Fibonacci", fibonacci],
    ["Fibonacci Call", fiboCall],
    ["Factorial Class", factorial],
    ["Find Factors", factors],
    ["Factors Tester", factorsTester], 
    ["Find Primes", primes],
    ["Primes Tester", primesTester],
    
]

fun_sub_menu = [
    ["Tree", tree],
    ["Ship", ship],
    ["Matrix", test_matrix],
    ["Swap", test_swap],
    ["For Loop", for_loop],
    ["While Loop", while_loop],
    ["Recursive Loop", recursive_loop],
]

week0_sub_menu = [
    ["Tree", tree],
    ["Ship", ship],
    ["Matrix", test_matrix],
    ["Swap", test_swap],
]

week1_sub_menu = [
    ["For Loop", for_loop],
    ["While Loop", while_loop],
    ["Recursive Loop", recursive_loop],
    ["Factorial", tester],
    ["Fibonacci", fibonacci],
]

week2_sub_menu = [
    ["Factorial Class", factorial],
    ["Find Factors", factors],
    ["Factors Tester", factorsTester], 
    ["Find Primes", primes],
    ["Primes Tester", primesTester],
    ["Fibonacci Call", fiboCall],
]


# def menu
def menu():
    title = "Main Menu"
    menu_list = main_menu.copy()
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Fun", fun_submenu])
    menu_list.append(["--------------"])
    menu_list.append(["Week 0", week0_submenu])
    menu_list.append(["Week 1", week1_submenu])
    menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)

# def submenu
def math_submenu():
    title = "Math Submenu"
    buildMenu(title, math_sub_menu)

def fun_submenu():
    title = "Fun Submenu" 
    buildMenu(title, fun_sub_menu)
  
def week2_submenu():
    title = "Week 2 Submenu"
    buildMenu(title, week2_sub_menu)
    
def week1_submenu():
    title = "Week 1 Submenu"
    buildMenu(title, week1_sub_menu)

def week0_submenu():
    title = "Week 0 Submenu" 
    buildMenu(title, week0_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '| ⇨ ', value[0])

    # get user choice
    choice = input("Type your choice ⊱ ")
    print()
    
    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try
    print()
    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
