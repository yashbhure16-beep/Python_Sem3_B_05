"""Program 2.1: basic functions."""

def greet(name):
    print('Hello, ' + name + '!')

def square(number):
    return number ** 2

def cube(number):
    return number ** 3
for name, number in [('Yash', 2), ('Dev', 3), ('Manav', 4)]:
    greet(name)
    print('Square of', number, ':', square(number))
    print('Cube of', number, ':', cube(number))
