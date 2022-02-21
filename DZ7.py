lst = [0, 9, 0, 6, 7, 9, 7, 8]
x = len(lst)
for i in range(x):
    if lst[i] == 0:
        del lst[i]
        lst.append(0)
print(lst)
print("-" * 30)
print("End")
