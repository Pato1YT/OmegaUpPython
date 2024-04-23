palabra = input()

palabra = str(palabra)

palabrai = palabra[::-1]

if palabra == palabrai:
    print("SI")
else:
    print("NO")