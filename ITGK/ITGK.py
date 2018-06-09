a = [1,2,3]
b = [] # b er en ny liste som ikke peker til a
for element in a:
    b.append(element)
print(a)
print(b)
print()
b[0] = 5
print(b)
print(a)

c = a #c peker til a
c[0] = 5
print()
print(c)
print(a)


a = [[1,2,3],[4,5,6]]
b = []
for i in range(len(a)):
    ny_element = []
    ny_element += a[i]
    b.append(ny_element)
b[0][0] = 7
print(a)
print(b)
