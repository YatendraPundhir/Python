# Global Variable
'''
l=20

def function1(n) :
    l=5
    print(l)
    print(n, "Hello ! your are inside a function")

function1("WAOOOOOOOO")
'''

# Global Keyword
l=20

def function1(n) :
    global l
    l= l+20
    print(l)
    print(n, "Hello ! your are inside a function")

function1("WAOOOOOOOO")