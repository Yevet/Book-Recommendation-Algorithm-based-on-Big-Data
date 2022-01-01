import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

author = ('Murakami', 'Higashino', 'J.K', 'Agatha', 'Cixin Liu', 'Yingtai', 'Yao Lu', 'Xiaobo Wang', 'Hua Yu')
grade = [8.15, 8.8, 8.93, 8.95, 9.1, 8.6, 9, 9, 9.1]

plt.bar(author, grade, width=0.1)
plt.xlabel("author")
plt.ylabel("ave_grade")
plt.title('The grade rank of nine excellent authors')



plt.savefig('author_average_rank.jpg')
plt.show()