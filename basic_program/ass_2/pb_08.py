a=5
print(type(a))
print(int(a))
print(float(a))
print(bool(a))
print(complex(a))
print(str(a))

b=3.4
print(type(b))
print(int(b))
print(float(b))
print(bool(b))
print(complex(b))
print(str(b))

c=True
print(type(c))
print(int(c))
print(float(c))
print(bool(c))
print(complex(c))
print(str(c))

d=3+5j
print(type(d))
try:
    print(int(d))
except TypeError:
    print('sorry')
try:    
    print(float(d))
except TypeError:
    print('sorry')
print(bool(d))
print(complex(d))
print(str(d))

e='hello'
print(type(e))
try:
    print(int(e))
except ValueError:
    print('sorry')
try:
    print(float(e))
except ValueError:
    print('sorry')
print(bool(e))
try:
    print(complex(e))
except ValueError:
    print('sorry')
print(str(e))


print("Cast to\t\tint\tfloat\tbool\tcomplex\tstr\nint\t\tP\tP\tP\tP\tP\nfloat\t\tP\tP\tP\tP\tP\nbool\t\tP\tP\tP\tP\tP\ncomplex\t\tN\tN\tP\tP\tP\nstr\t\tN\tN\tP\tN\tP")
