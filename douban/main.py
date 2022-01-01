import sys
import getopt
import pandas as pd
from get_cookies import get_cookies
from book_wordcloud import book_wordcloud
from emotion_analysis import emotion_analysis


def main():
    #获取url和cookies
    #url是每本书的网址
    url = 'https://book.douban.com/subject/1826007/'
    cookies = get_cookies()
    
    #调用函数
    emotion_analysis(url, cookies)
    #
    book_wordcloud(url, cookies)

if __name__ == "__main__":
    main()
