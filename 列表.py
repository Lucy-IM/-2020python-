# li=[] #空列表
# li=[1,2,3,"你好"]
# print(len(li)) #len函数可以获取到列表对象中的数据个数
# strA='我喜欢python'
# print(len(strA))
# print(type(li))
# 查找
listA=['abcd',785,12.23,'qiuzhi',True]
# print(listA) #输出完整的列表
# print(listA[0]) #输出第一个元素
# print(listA[1:3]) #从第二个开始到第三个元素
# print(listA[2:]) #从第三个元素开始到最后所有的元素
# print(listA[::-1]) #负数从右像左开始输出
# print(listA*3) #输出多次列表中的数据【复制】
# print('--------------增加-----------------------')
# print('追加之前',listA)
# listA.append(['fff','ddd']) #追加操作
# listA.append(8888)
# print('追加之后',listA)
# listA.insert(1,'这是我刚插入的数据') #插入操作 需要执行一个位置插入
# print(listA)
# rsData=list(range(10)) #强制转换为list对象
# print(type(rsData))
# listA.extend(rsData) #拓展  等于批量添加
# listA.extend([11,22,33,44])
# print(listA)
# print('-----------------修改------------------------')
# print('修改之前',listA)
# listA[0]=333.6
# print('修改之后',listA)
listB=list(range(10,50))

print('------------删除list数据项------------------')
print(listB)
# del listB[0] #删除列表中第一个元素
# del listB[1:3] #批量删除多项数据 slice
# listB.remove(20) #移除指定的元素  参数是具体的数据值
listB.pop(1) #移除制定的项  参数是索引值
print(listB)

print(listB.index(19,20,25))  #返回的是一个索引下标


