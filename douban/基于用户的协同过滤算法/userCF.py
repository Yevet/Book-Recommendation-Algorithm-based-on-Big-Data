# encoding=utf-8
from math import sqrt
import codecs

def loadData():
    # 训练集
    trainSet = {}
    # 看过该本书的所有用户集合
    bookUser = {}
    # 用户-用户共有书籍矩阵
    u2u = {}

    TrainFile = '/home/hadoop/ratings.csv'

    # 加载训练集
    # trainset {"userName", {"bookName, rating"}}
    # bookUser {"bookName", ["username1", "username2", ...]} 即为物品-用户倒排表
    f = codecs.open(TrainFile, "r", "utf-8")
    lines = f.readlines()[1:30000] #第一行是标题
    for line in lines:
        (userName, bookName, rating) = line.strip().split(',')
        trainSet.setdefault(userName, {})
        trainSet[userName].setdefault(bookName, float(rating))
        bookUser.setdefault(bookName, [])
        bookUser[bookName].append(userName.strip())

    # 生成用户-用户共有书籍矩阵
    for b in bookUser.keys():
        # 遍历特定的书籍中所有的用户
        for u in bookUser[b]:
            u2u.setdefault(u, {})
            for n in bookUser[b]:
                if u != n:
                    u2u[u].setdefault(n,[])
                    u2u[u][n].append(b)

    return trainSet, u2u

def getAverageRating(user, trainSet):
    average = (sum(trainSet[user].values())*1.0) / len(trainSet[user].keys())
    return average

# 计算用户相似度
def getUserSim(u2u, trainSet):
    userSim = {}
    # 计算用户相似度
    # 对每个用户u
    for u in u2u.keys():
        if u != '':
            # 将用户u加入userSim中设为key，该用户对应一个字典
            userSim.setdefault(u, {})
            # 获取用户u对电影的平均评分
            average_u_rate = getAverageRating(u, trainSet)
            # 对与用户u相关的每个用户n
            for n in u2u[u].keys():
                if n != '':
                    # 将用户n加到用户u的字典中
                    userSim[u].setdefault(n,0)
                    # 获取用户n对电影的平均评分
                    average_n_rate = getAverageRating(n, trainSet)
                    # 皮尔逊相关系数的分子部分
                    part1 = 0
                    # 皮尔逊相关系数的分母的一部分
                    part2 = 0
                    # 皮尔逊相关系数的分母的一部分
                    part3 = 0
                    # 对用户u和用户n的共有的每个电影
                    for m in u2u[u][n]:
                        part1 += (trainSet[u][m] - average_u_rate) * (trainSet[n][m] - average_n_rate) * 1.0
                        part2 += pow(trainSet[u][m] - average_u_rate, 2) * 1.0
                        part3 += pow(trainSet[n][m] - average_n_rate, 2) * 1.0

                    part2 = sqrt(part2)
                    part3 = sqrt(part3)
                    # 若分母为0，相似度为0
                    if part2 == 0 or part3 == 0:
                        userSim[u][n] = 0
                    else:
                        userSim[u][n] = part1 / (part2 * part3)
    return userSim

# 寻找用户最近邻并生成推荐结果
def getRecommendations(N, trainSet, userSim):
    pred = {}
    # 对每个用户
    for user in trainSet.keys():
        # 生成空预测表
        pred.setdefault(user, {})
        # 获取该用户评过分的书籍
        interacted_items = trainSet[user].keys()
        # 获取该用户的平均评分
        average_u_rate = getAverageRating(user, trainSet)
        userSimSum = 0
        # 选取N个最相似的用户
        # lambda x:x[1] 根据用户相似度进行比较
        if user.strip() != '':
            simUser = sorted(userSim[user.strip()].items(), key=lambda x: x[1], reverse=True)[0:N]
            # 遍历相似用户的用户名和相似度
            for n, sim in simUser:
                # 得到该近邻用户的平均评分
                average_n_rate = getAverageRating(n, trainSet)
                # 对该用户所有近邻用户相似度求和
                userSimSum += sim 
                # 遍历该近邻用户的所有评分书籍和具体评分
                for m, nrating in trainSet[n].items():
                    # 如果这本书该用户已经看过，则跳过
                    if m in interacted_items:
                        continue
                    # 否则将这本书以及这本书的推荐指数加到这名用户的推荐列表中
                    else:
                        pred[user].setdefault(m, 0)
                        pred[user][m] += (sim * (nrating - average_n_rate))
            # 遍历这名用户推荐列表中的所有书籍，更新评分预测
            for m in pred[user].keys():
                if userSimSum == 0:
                    pred[user][m] = average_u_rate
                else:
                    pred[user][m] = average_u_rate + (pred[user][m] * 1.0) / userSimSum
    return pred

if  __name__ == '__main__':
    trainSet, u2u = loadData()
    userSim = getUserSim(u2u, trainSet)
    results = getRecommendations(10, trainSet, userSim)
    username = '100'
    sorted_results = sorted(results[username].items(),key=lambda x:x[1],reverse=True)[0:3]
    print(sorted_results)
    print(userSim['100']) 
