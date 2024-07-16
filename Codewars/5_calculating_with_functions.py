right = 0

def zero(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 0 + right
            case '-':
                return 0 - right
            case '*':
                return 0 * right
            case '/':
                return 0 // right
    else:
        right = 0
        return 0

def one(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 1 + right
            case '-':
                return 1 - right
            case '*':
                return 1 * right
            case '/':
                return 1 // right
    else:
        right = 1
        return 1
    
def two(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 2 + right
            case '-':
                return 2 - right
            case '*':
                return 2 * right
            case '/':
                return 2 // right
    else:
        right = 2
        return 2
    
def three(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 3 + right
            case '-':
                return 3 - right
            case '*':
                return 3 * right
            case '/':
                return 3 // right
    else:
        right = 3
        return 3
    
def four(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 4 + right
            case '-':
                return 4 - right
            case '*':
                return 4 * right
            case '/':
                return 4 // right
    else:
        right = 4
        return 4
    
def five(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 5 + right
            case '-':
                return 5 - right
            case '*':
                return 5 * right
            case '/':
                return 5 // right
    else:
        right = 5
        return 5
    
def six(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 6 + right
            case '-':
                return 6 - right
            case '*':
                return 6 * right
            case '/':
                return 6 // right
    else:
        right = 6
        return 6
    
def seven(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 7 + right
            case '-':
                return 7 - right
            case '*':
                return 7 * right
            case '/':
                return 7 // right
    else:
        right = 7
        return 7
    
def eight(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 8 + right
            case '-':
                return 8 - right
            case '*':
                return 8 * right
            case '/':
                return 8 // right
    else:
        right = 8
        return 8

def nine(x=None):
    global right
    if x:
        op = x
        match op:
            case '+':
                return 9 + right
            case '-':
                return 9 - right
            case '*':
                return 9 * right
            case '/':
                return 9 // right
    else:
        right = 9
        return 9
    
def plus(x):
    return '+'

def minus(x):
    return '-'

def times(x):
    return '*'

def divided_by(x):
    return '/'




# print(four(plus(nine())))

print(nine(minus(nine())))