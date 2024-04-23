import itertools

list = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

for i in itertools.count():
    op = int(input())
    
    if op <= 0:
        break
    elif op in list:
        print("existe")
    else:
        print("no existe")
        