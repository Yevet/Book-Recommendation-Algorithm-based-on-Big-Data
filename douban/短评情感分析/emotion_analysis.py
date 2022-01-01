from wordfilter import wordfiter
from snownlp import SnowNLP
import numpy as np
import requests
import bs4

# 情感分析
def emotion_analysis(url, cookies):
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
		# 找到该页所有短评
		soup_list = soup.findAll('p', attrs={'class': 'comment-content'})
		for com in soup_list:
			comment = com.find('span').string
			comment_list.append(comment)
		print('第%d页短评已采集' % page_num)
		if page_num > 19:
			print('采集完毕，情感分析中')
			break
	marks_list = []
	for com in comment_list:
		mark = SnowNLP(com)
		marks_list.append(mark.sentiments)
	
	#snownlp得出的情感分数，1为正面情绪（也就是好评，0为负面情绪（即为差评
	print('情感分数：', np.mean(marks_list))
	
	#plt.plot( np.arange(1, 401, 1), marks_list)
	#plt.xlabel('number of page')
	#plt.ylabel('score')
	#plt.show()