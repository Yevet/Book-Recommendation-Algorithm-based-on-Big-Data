
# 获得cookies值
def get_cookies():
	# 打开所保存的cookies内容文件  
	f=open('/home/hadoop/douban/cookies.txt', 'r')
	cookies={}
	for line in f.read().split(';'):
		name, value = line.strip().split('=', 1)
		cookies[name]=value 
	return cookies
