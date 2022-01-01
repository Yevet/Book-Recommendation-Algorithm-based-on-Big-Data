import numpy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from PIL import Image
# 生成词云
def create_word_cloud():
    frequencies = {}
    for line in open("/home/hadoop/book_analyze/popular.txt",encoding='utf-8'):
        #comp1 = re.compile('\x00')
        #get = comp1.sub(' ', get)
        arr = line.split("$$")
        frequencies[arr[0]] = float(arr[1])
    color_mask=numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))
    wc = WordCloud(
        mask=color_mask,
        font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
        max_words=200,
        background_color="white"
        #width=2000,
        #height=1200,

    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("/home/hadoop/book_analyze/popular_wordcloud.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    frequencies = {}
    for line in open("/home/hadoop/book_analyze/economic.txt", encoding='utf-8'):
        # comp1 = re.compile('\x00')
        # get = comp1.sub(' ', get)
        arr = line.split("$$")
        frequencies[arr[0]] = float(arr[1])
    color_mask = numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))
    wc = WordCloud(
        mask=color_mask,
        font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
        max_words=200,
        background_color="white"
        # width=2000,
        # height=1200,

    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("/home/hadoop/book_analyze/economic_wordcloud.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    frequencies = {}
    for line in open("/home/hadoop/book_analyze/technology.txt", encoding='utf-8'):
        # comp1 = re.compile('\x00')
        # get = comp1.sub(' ', get)
        arr = line.split("$$")
        frequencies[arr[0]] = float(arr[1])
    color_mask = numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))
    wc = WordCloud(
        mask=color_mask,
        font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
        max_words=200,
        background_color="white"
        # width=2000,
        # height=1200,

    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("/home/hadoop/book_analyze/technology_wordcloud.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    frequencies = {}
    for line in open("/home/hadoop/book_analyze/life.txt", encoding='utf-8'):
        # comp1 = re.compile('\x00')
        # get = comp1.sub(' ', get)
        arr = line.split("$$")
        frequencies[arr[0]] = float(arr[1])
    color_mask = numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))
    wc = WordCloud(
        mask=color_mask,
        font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
        max_words=200,
        background_color="white"
        # width=2000,
        # height=1200,

    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("/home/hadoop/book_analyze/life_wordcloud.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    frequencies = {}
    for line in open("/home/hadoop/book_analyze/culture.txt", encoding='utf-8'):
        # comp1 = re.compile('\x00')
        # get = comp1.sub(' ', get)
        arr = line.split("$$")
        frequencies[arr[0]] = float(arr[1])
    color_mask = numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))
    wc = WordCloud(
        mask=color_mask,
        font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
        max_words=200,
        background_color="white"
        # width=2000,
        # height=1200,

    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("/home/hadoop/book_analyze/culture_wordcloud.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    frequencies = {}
    for line in open("/home/hadoop/book_analyze/literature.txt", encoding='utf-8'):
        # comp1 = re.compile('\x00')
        # get = comp1.sub(' ', get)
        arr = line.split("$$")
        frequencies[arr[0]] = float(arr[1])
    color_mask = numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))
    wc = WordCloud(
        mask=color_mask,
        font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
        max_words=200,
        background_color="white"
        # width=2000,
        # height=1200,

    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("/home/hadoop/book_analyze/literature_wordcloud.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    frequencies = {}
    for line in open("/home/hadoop/book_analyze/book.txt", encoding='utf-8'):
        # comp1 = re.compile('\x00')
        # get = comp1.sub(' ', get)
        arr = line.split("$$")
        frequencies[arr[0]] = float(arr[1])
    color_mask = numpy.array(Image.open('/home/hadoop/book_analyze/map.png'))
    wc = WordCloud(
        mask=color_mask,
        font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
        max_words=1000,
        background_color="white"
        # width=2000,
        # height=1200,

    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("/home/hadoop/book_analyze/book_wordcloud.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

# 根据词频生成词云
create_word_cloud()