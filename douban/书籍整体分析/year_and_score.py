from pyecharts import Bar,Pie,Map,WordCloud
from pylab import *
from pyecharts import *

lines = []
a1=0;b1=0;a2=0;b2=0;a3=0;b3=0;a4=0;b4=0;a5=0;b5=0;a6=0;b6=0;a7=0;b7=0;a8=0;b8=0;a9=0;b9=0;a10=0;b10=0;
a11=0;b11=0;a12=0;b12=0;a13=0;b13=0;a14=0;b14=0;a15=0;b15=0;a16=0;b16=0;a17=0;b17=0;a18=0;b18=0;a19=0;b19=0;a20=0;b20=0;
a21=0;b21=0;a22=0;b22=0;a23=0;b23=0;a24=0;b24=0;a25=0;b25=0;a26=0;b26=0;a27=0;b27=0;a28=0;b28=0;a29=0;b29=0;a30=0;b30=0;
a31=1;b31=1;a32=1;b32=1;a33=1;b33=1;a34=1;b34=1;a35=1;b35=1;a36=1;b36=1;a37=1;b37=1;a38=1;b38=1;a39=1;b39=1;a40=1;b40=1;
a41=0;b41=0;a42=0;b42=0;a43=0;b43=0;a44=0;b44=0;

with open('/home/hadoop/writer_world.txt', 'r', encoding='utf-8') as file_to_read:
        while True:
            line = file_to_read.readline()
            #line=line.replace('\n','')
            line=line.strip("\n")
            line=line.strip()
            if not line:
                break
            arr = line.split('$$$')
            if(('(美)' in arr[0])|('(美国)' in arr[0])):
                a1=a1+float(arr[1])
                b1=b1+1
            elif(('[日]' in arr[0])|('(日)' in arr[0])):
                a2 = a2 + float(arr[1])
                b2 = b2 + 1
            elif(('[法]' in arr[0])|('(法)' in arr[0])):
                a3 = a3 + float(arr[1])
                b3 = b3 + 1
            elif (('[英]' in arr[0]) | ('(英)' in arr[0])|('(英国)' in arr[0])):
                a4 = a4+ float(arr[1])
                b4 = b4 + 1
            elif (('[德]' in arr[0]) | ('(德)' in arr[0])|('(联邦德国)' in arr[0])):
                a5 = a5 + float(arr[1])
                b5 = b5 + 1
            elif (('[荷]' in arr[0]) | ('(荷)' in arr[0])):
                a6 = a6 + float(arr[1])
                b6 = b6 + 1
            elif (('(阿根廷)' in arr[0]) ):
                a7 = a7 + float(arr[1])
                b7 = b7 + 1
            elif (('( 新加坡 )' in arr[0])| ('(新加坡)' in arr[0])):
                a8 = a8 + float(arr[1])
                b8 = b8 + 1
            elif (('(爱尔兰)' in arr[0]) ):
                a9 = a9 + float(arr[1])
                b9 = b9 + 1
            elif (('(奥)' in arr[0]) ):
                a10 = a10 + float(arr[1])
                b10 = b10 + 1
            elif (('(澳)' in arr[0])|('(澳大利亚)' in arr[0]) ):
                a11 = a11 + float(arr[1])
                b11 = b11 + 1
            elif (('(巴西)' in arr[0])):
                a12 = a12 + float(arr[1])
                b12 = b12 + 1
            elif (('(比)' in arr[0])):
                a13 = a13 + float(arr[1])
                b13 = b13 + 1
            elif (('(波)' in arr[0])|('(波兰)' in arr[0])):
                a14 = a14 + float(arr[1])
                b14 = b14 + 1
            elif (('(波黑)' in arr[0])):
                a15 = a15 + float(arr[1])
                b15 = b15 + 1
            elif (('(波斯)' in arr[0])|('(伊朗)' in arr[0])):
                a16 = a16 + float(arr[1])
                b16 = b16 + 1
            elif (('(丹)' in arr[0])|('(丹麦)' in arr[0])):
                a17 = a17 + float(arr[1])
                b17 = b17 + 1
            elif (('(俄)' in arr[0])|('(俄罗斯)' in arr[0])|('(前苏联)' in arr[0])|('(苏)' in arr[0])|('(苏联)' in arr[0])):
                a18 = a18 + float(arr[1])
                b18 = b18 + 1
            elif (('(古希腊)' in arr[0])|('(希腊)' in arr[0])):
                a19 = a19 + float(arr[1])
                b19 = b19 + 1
            elif ('(韩)' in arr[0]):
                a20 = a20 + float(arr[1])
                b20 = b20 + 1
            elif (('(加)' in arr[0])|('(加拿大)' in arr[0])):
                a21 = a21 + float(arr[1])
                b21 = b21 + 1
            elif (('(捷)' in arr[0])|('(捷克)' in arr[0])):
                a22 = a22 + float(arr[1])
                b22 = b22 + 1
            elif ('(肯尼亚)' in arr[0]):
                a23 = a23 + float(arr[1])
                b23 = b23 + 1
            elif ('(黎巴嫩)' in arr[0]):
                a24 = a24 + float(arr[1])
                b24 = b24 + 1
            elif ('(罗马尼亚)' in arr[0]):
                a25 = a25 + float(arr[1])
                b25 = b25 + 1
            elif (('(孟)' in arr[0])|('(孟加拉)' in arr[0])):
                a26 = a26 + float(arr[1])
                b26 = b26 + 1
            elif (('(秘)' in arr[0])|('(秘鲁)' in arr[0])):
                a27 = a27 + float(arr[1])
                b27 = b27 + 1
            elif (('(摩洛哥)' in arr[0])):
                a28 = a28 + float(arr[1])
                b28 = b28 + 1
            elif (('(墨)' in arr[0])|('(墨西哥)' in arr[0])):
                a29 = a29 + float(arr[1])
                b29 = b29 + 1
            elif (('(挪)' in arr[0])|('(挪威)' in arr[0])):
                a30 = a30 + float(arr[1])
                b30 = b30 + 1
            elif (('(葡萄牙)' in arr[0])|('(葡)' in arr[0])):
                a31 = a31 + float(arr[1])
                b31 = b31 + 1
            elif ('(瑞典)' in arr[0]):
                a32 = a32 + float(arr[1])
                b32 = b32 + 1
            elif ('(瑞士)' in arr[0]):
                a33 = a33 + float(arr[1])
                b33 = b33 + 1
            elif ('(土耳其)' in arr[0]):
                a34 = a34 + float(arr[1])
                b34 = b34 + 1
            elif ('(委日瑞拉)' in arr[0]):
                a35 = a35 + float(arr[1])
                b35 = b35 + 1
            elif ('(乌拉圭)' in arr[0]):
                a36 = a36 + float(arr[1])
                b36 = b36 + 1
            elif (('(西)' in arr[0])|('(西班牙)' in arr[0])):
                a37 = a37 + float(arr[1])
                b37 = b37 + 1
            elif ('(新西兰)' in arr[0]):
                a38 = a38 + float(arr[1])
                b38 = b38 + 1
            elif (('(匈)' in arr[0])|('(匈牙利)' in arr[0])):
                a39 = a39 + float(arr[1])
                b39 = b39 + 1
            elif (('(以)' in arr[0])|('(以色列)' in arr[0])):
                a40 = a40 + float(arr[1])
                b40 = b40 + 1
            elif (('(意)' in arr[0])|('(意大利)' in arr[0])):
                a41 = a41 + float(arr[1])
                b41 = b41 + 1
            elif (('(印)' in arr[0])|('(印度)' in arr[0])):
                a42 = a42 + float(arr[1])
                b42 = b42 + 1
            elif ('(阿富汗)' in arr[0]):
                a43 = a43 + float(arr[1])
                b43 = b43 + 1
            else:
                a44 = a44 + float(arr[1])
                b44 = b44 + 1

value1 = [a1/b1,a2/b2,a3/b3,a4/b4,a5/b5,a6/b6,a7/b7,a8/b8,a9/b9,a10/b10
         ,a11/b11,a12/b12,a13/b13,a14/b14,a16/b16,a17/b17,a18/b18,a19/b19,a20/b20
         ,a21/b21,a22/b22,a23/b23,a24/b24,a25/b25,a26/b26,a27/b27,a28/b28,a29/b29,a30/b30
        ,a31/b31,a32/b32,a33/b33,a34/b34,a35/b35,a36/b36,a37/b37,a38/b38,a39/b39,a40/b40
        ,a41/b41,a42/b42,a43/b43,a44/b44
         ]

#为了使数据差异更明显在此处做了放大差距的处理
value = [(i-8)*130 for i in value1]

attr = ["United States","Japan","France","United Kingdom","Germany","Netherlands","Argentina", "Singapore", "Ireland", "Austria",
        "Australia", "Brazil", "Belgium", "Poland", "Iran", "Denmark", "Russia", "Greece", "South Korea",
        "Canada", "Czech Republic", "Kenya", "Lebanon", "Romania", "Bangladesh", "Peru","Morocco", "Mexico", "Norway",
        "Portugal", "Sweden", "Switzerland", "Turkey", "Venezuela", "Uruguay", "Spain", "New Zealand", "Hungary","Israel",
        "Italy","India", "Afghanistan","China"
        ]
map0 = Map("世界地图示例", width=1200, height=600)

map0.add("世界地图", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000',min=800)
map0.visualMap: {
            min: 800,
            max: 50000,
        }
map0.render(path="/home/hadoop/average score of writers.html")


