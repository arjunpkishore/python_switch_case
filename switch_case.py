def case(arg):
    switch={
        1 : "case 1"
        2 : "case 2"
        'x' : "case x"
        'y' : "case y"
        'default' : "unknown case"
    }
    return switch.get(arg, switch['default'])
