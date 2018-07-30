def cube(number):
    return number**3
def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False

print cube(2)
print by_three(3)
