def case(arg):
    switch={
        1 : "case 1",
        2 : "case 2",
        'x' : "case x",
        'y' : "case y",
        'default' : "unknown case"
    }
    return switch.get(arg, switch['default'])


def case_1():
    return "Return Case 1 Output"

def case_2():
    return "Return Case 2 Output"

def case_x():
    return "Return Case x Output"

def case_y():
    return "Return Case y Output"

def fun_case(arg):
    switch={
        1 : case_1,
        2 : case_2,
        'x' : case_x,
        'y' : case_y
     }
    func = switch.get(arg, lambda:"Return Uknown Case output")
    return func()

print case(1)
print case('x')


print fun_case(5)
print fun_case('y')
