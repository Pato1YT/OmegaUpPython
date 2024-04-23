n = int(input())

list = []

for i in range(n):
    i = str(input())
    list.append(i)
    
for elem in list:
    if '/'  in elem:
        list.remove(elem)
    elif '*/' in elem:
        list.remove(elem)
    elif '/*' in elem:
        list.remove(elem)
        
for elem2 in list:
    print(elem2)