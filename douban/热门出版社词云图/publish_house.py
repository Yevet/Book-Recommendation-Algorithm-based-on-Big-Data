import numpy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from PIL import Image

# 生成词云
for line in open("/home/hadoop/book_analyze/publishhouse.txt", encoding='utf-8'):
    arr = line.split("/")
    f = open('/home/hadoop/book_analyze/publish_after_washing.txt', 'a', encoding='utf-8')
    f.writelines(arr[0])
    f.write('\n')
f.close()
color_mask = numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))

with open('/home/hadoop/book_analyze/publish_after_washing.txt', encoding='utf-8') as f:  # 默认模式为‘r’，只读模式
    contents = f.read()  # 读取文件全部内容

wc = WordCloud(
    mask=color_mask,
    font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
    max_words=100,
    background_color="white",
    # width=2000,
    # height=1200
).generate(contents)

# 显示词云文件
plt.imshow(wc)
plt.axis("off")
plt.savefig("/home/hadoop/book_analyze/hot_publishhouse_wordcloud.jpg")
plt.show()
