from wordcloud import WordCloud
from wordfilter import wordfiter
import matplotlib.pyplot as plt
import requests
import jieba
import bs4


# 制作词云
def book_wordcloud(url, cookies):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'
		}
	page_num = 0
	comment_list = []
	while True:
		page_num += 1
		url = url + 'comments/?start={}&limit=20&status=P&sort=new_score'.format(str(page_num*20))
		res = requests.get(url, cookies=cookies, headers=headers)
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		# 找到该页的comment-content
		soup_list = soup.findAll('p', attrs={'class': 'comment-content'})
		for com in soup_list:
			comment = com.find('span').string
			comment_list.append(comment)
		print('第%d页短评已采集' % page_num)
		if page_num > 5:
			print('采集完毕，制作词云中')
			break
	all_comments = []
	for hc in comment_list:
		hc = jieba.lcut(hc)
		#print(atype(hc))
		hc = wordfiter(hc)
		all_comments += hc
	#all_comments = wordfiter(all_comments)
	words = ' '.join(all_comments)
	#print(words)
	# 设置字体和背景颜色
	Words_Cloud = WordCloud(font_path='/home/hadoop/douban/simkai.ttf', background_color='white').generate(words)
	Words_Cloud.to_file('/home/hadoop/douban/results/wordcloud for book comment.jpg')





