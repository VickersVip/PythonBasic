people_num = {
    'john' : 12,
    'chou' : 38,
    'vickers' : 88,
    'liu' : 33,
    'jack' : 13
}

#第一种遍历字典的方式,遍历键和值
""""
for keys,values in people_num.items():
    print(keys + "like the number of" + str(values))
"""


#第二中遍历字典的方式,遍历键
for keys in people_num.keys():
    print(keys + "like the number of" + str(people_num[keys]))


