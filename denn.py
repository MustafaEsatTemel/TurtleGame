funcs = []
for i in range(5):
    funcs.append(lambda: i)

for func in funcs:
    print(func())