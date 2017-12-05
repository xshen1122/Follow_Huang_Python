# test_collections.py
# coding: utf-8
'''
提供了几个额外的数据类型
1.namedtuple(): 生成可以使用名字来访问元素内容的tuple子类

2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
	l.insert(0, v)
	l.pop(0)
	deque.rotate()

3.Counter: 计数器，主要用来计数

4.OrderedDict: 有序字典
5.defaultdict: 带有默认值的字典

'''
from collections import namedtuple
from collections import deque
import sys
import time
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
def testNamedtuple():
	websites = [
	    ('Sohu', 'http://www.google.com/', u'张朝阳'),
	    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
	    ('163', 'http://www.163.com/', u'丁磊')
	]
	Website = namedtuple('Website', ['name', 'url', 'founder'])
	for website in websites:
	    website = Website._make(website)
	    print website


def paoMadeng():
	fancy_loading = deque('>--------------------')
	while True:
	    print '\r%s' % ''.join(fancy_loading),
	    fancy_loading.rotate(1)
	    sys.stdout.flush()
	    time.sleep(0.08)

def Top5():

	s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()
	c = Counter(s)
	# 获取出现频率最高的5个字符
	print c.most_common(5)

def test_OrderDict():
	items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
	)
	regular_dict = dict(items)
	ordered_dict = OrderedDict(items)
	print 'Regular Dict:'
	for k, v in regular_dict.items():
	    print k, v
	print 'Ordered Dict:'
	for k, v in ordered_dict.items():
	    print k, v

def test_defaultdict():
	members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
	]
	result = defaultdict(list)
	for sex, name in members:
	    result[sex].append(name)
	print result

if __name__ == '__main__':
	test_defaultdict()