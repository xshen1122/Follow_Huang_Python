# test_format.py
# coding:utf-8

# 最最常用的
print 'hello {0}'.format('Nihao')
print 'hello {0} i am {1}'.format('Kevin','Tom')                  # hello Kevin i am Tom
print 'hello {} i am {}'.format('Kevin','Tom')                    # 不标明顺序也行，hello Kevin i am Tom
print 'hello {0} i am {1} . my name is {0}'.format('Kevin','Tom') # 可以多次填充


#通过key来填充 ， 使用不多吧。
print 'hello {name1}  i am {name2}'.format(name1='Kevin',name2='Tom')

#通过下标填充，使用不多吧
names=['Kevin','Tom']
print 'hello {names[0]}  i am {names[1]}'.format(names=names)                  # hello Kevin i am Tom
print 'hello {0[0]}  i am {0[1]}'.format(names)

#通过字典的key
names={'name':'Kevin','name2':'Tom'}
print 'hello {names[name]}  i am {names[name2]}'.format(names=names)  

#通过对象的属性
class Names():
    name1='Kevin'
    name2='Tom'
 
print 'hello {names.name1}  i am {names.name2}'.format(names=Names) 

#使用魔法参数
args=['lu']
kwargs = {'name1': 'Kevin', 'name2': 'Tom'}
print 'hello {name1} {} i am {name2}'.format(*args, **kwargs) 

