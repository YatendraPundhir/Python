# For loop programs

list = [["Ajay" , 1],["Amar",6],["Anuj",10],["avi",20]]

for item in list:
   print(item)

for item in list:
   print(list)

for item, lolipop in list:
    print(item , lolipop)


items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
