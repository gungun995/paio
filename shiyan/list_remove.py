a = [1, 2, 3, 4, 5]
b = [3, 4, 5]
for i in a:
    if i in b:
        a.remove(i)
print(a)
# [1, 2, 4]
