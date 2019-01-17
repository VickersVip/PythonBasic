vocabulary = {
    'patch':'补丁',
    'session':'会话',
    'request':'请求',
    'abstract':'抽象的',
    'append':'附加的'
}

print('第一种显示方式')
for keys in vocabulary.keys():
    print(keys + ': ' + vocabulary[keys])

print('第二中显示方式')
for keys,values in vocabulary.items():
    print(keys)
