import numpy as np
import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
#plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = 0
y = 0
z = 0
a = 0
b = 0
c = 0

for line in open("/home/hadoop/book_analyze/booktype.txt", encoding='utf-8'):
    if line.strip() == 'culture':
        x = x + 1
    elif line.strip() == 'literature':
        y = y + 1
    elif line.strip() == 'popular':
        z = z + 1
    elif line.strip() == 'life':
        a = a + 1
    elif line.strip() == 'technology':
        b = b + 1
    elif line.strip() == 'economic':
        c = c + 1
    else:
        print(a)

labels = 'culture', 'literature', 'popular', 'life', 'technology', 'economic'
fraces = [x, y, z, a, b, c]

plt.axes(aspect=1)
plt.pie(x=fraces, labels=labels, autopct='%0f%%', shadow=True)
plt.savefig('/home/hadoop/book_analyze/book_type.jpg')
plt.show()