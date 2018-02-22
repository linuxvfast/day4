__author__ = 'linux vfast'
'''
list1 = ['li','wang','zhang','yang','li','zhang',1,2]

list2 = [1,2,3,4,1,2,3]

set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
#并集
print(set1|set2)
print(set1.union(set2))
#交集
print(set1&set2)
print(set1.intersection(set2))
#差集
print(set1.difference(set2))
print(set2.difference(set1))
print('------------------')
print(set1 - set2)
#子集
print(set1.issubset(set2))

list3 = [1,2]
set3 = set(list3)
print(set2.issubset(set3))
#父集
print(set2.issuperset(set3))

#对称差集
print(set2.symmetric_difference(set3))
print('--------------')
print(set2 ^ set3)

# set3.remove(1)
# print(set3)
'''

#对比discart和remove
list3 = [1,2]
set3 = set(list3)
# set3.pop()
set3.discard(4)   #discard不报错
# set3.remove(4)  #remove参数为空或者不存在的值报错
print(set3)