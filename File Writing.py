#f = open("yatendra.txt")
#content = f.read()
#print(content)
#f.close()

with open("yatendra.txt") as f:
    a = f.readlines()
    print(a)