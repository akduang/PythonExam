# # #1

# # def hello():
# #     return "Hello, World!"
  
# # # Too slow 
# # # change

# a = [3,1,1]
# range(10)
# # [1,10)
# b = list((3,1,2))
# c = list(range(10))
# print(type(a),type(b),type(c))

# #正索引(0-5)，负索引(-5--1)
# #切片  : s 位宽
# # list 的复制是副本  浅拷贝
# b = a[:]
#反转
# a[start:end:step]
a = [3,7,4,2,6]

#正负 

a[::-1]
# 少 append(最后) insert(指定) insert(位置，值)
# 批量 extend
# pop 最后一个
# remove 指定值
# del 索引

#遍历
b = len(a)

update_list = [e*2 for e in one_list]
#eval() 转换
# 字典 get方法 访问