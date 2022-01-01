from pylab import *


lines = []
with open('/home/hadoop/allbookscore.txt', 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(float(line))

plt.figure(figsize=(25,12)) #初始化一张图
x = lines
plt.hist(x, bins='auto', rwidth=80)  #直方图关键操作
#plt.bins=400
#plt.xticks(np.arange(2,10,0.1))
#mpl.rcParams['font.sans-serif']=['SimHei']
plt.grid(alpha=2,linestyle='-.') #网格线，更好看
plt.grid(alpha=2,linestyle='-.') #网格线，更好看
plt.ylabel('Time', fontdict={'weight': 'normal', 'size': 25})
plt.xlabel('Time', fontdict={'weight': 'normal', 'size': 25})
plt.yticks(fontsize=25)
plt.xticks(fontsize=25)
#plt.title(r'豆瓣书籍评分频数分布图',fontdict={'weight':'normal','size': 35}) #改变图标题字体
plt.xlabel('score')
plt.ylabel('book\'s number')
plt.savefig('/home/hadoop/pinshufenbu.jpg')
plt.show()

