# Higher Order Function - A function can be passed as argument, return as output
def small(txt):
    return txt.lower()
def capital(txt):
    return txt.upper()
def all(func):
    greeting = func("Hi This is Ram, programming for function as an argument")
    print(greeting)
all(small)
all(capital)