truth = True
lie = False
print(type(truth)) # <class 'bool'>
print(type(lie)) # <class 'bool'>

print(0 == 0) # True
print(0 > 0) # False

print(bool("pddu")) # True
print(bool("")) # False
print(bool([1, 2])) # True
print(bool([])) # False
print(bool((1, 2))) # True
print(bool(())) # False
print(bool({'num': 1})) # True
print(bool({})) # False
print(bool(1)) # True
print(bool(0)) # False
print(bool(None)) # False

