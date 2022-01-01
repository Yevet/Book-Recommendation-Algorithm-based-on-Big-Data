#删除停用词（为制作词云和情感分析做基础）
def wordfiter(sequence):
    stopwords = [line.strip() for line in open('/home/hadoop/douban/stop_words.txt', 'r', encoding='utf-8').readlines()]
    #print(stopwords)
    data = []
    for word in sequence:
        if word not in stopwords:
            if word !='\t' :
                data.append(word)
    #print(data)
    return data
