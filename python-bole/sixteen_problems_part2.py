# sixteen_problems_part2.py
# coding: utf-8
'''
构造器

'''
class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName
    def __repr__(self):
        return "<Node '{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
    def print_all_1(self):
        print self
        for oChild in self._lChildren:
            oChild.print_all_1()
    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print oNode
'''
10.    如何用Python来进行查询和替换一个文本字符串？
 答：可以使用re模块中的sub()函数或者subn()函数来进行查询和替换，

格式：sub(replacement, string[,count=0])
（replacement是被替换成的文本，string是需要被替换的文本，count是一个可选参数，指最大被替换的数量）

'''

'''
15.    如何在一个function里面设置一个全局的变量？

答：解决方法是在function的开始插入一个global声明：

def f()

global x

'''




if __name__ == '__main__':
	# oRoot = Node('root')
	# oChild1 = Node("child1")
	# oChild2 = Node("child2")
	# oChild3 = Node("child3")
	# oChild4 = Node("child4")
	# oChild5 = Node("child5")
	# oChild6 = Node("child6")
	# oChild7 = Node("child7")
	# oChild8 = Node("child8")
	# oChild9 = Node("child9")
	# oChild10 = Node("child10")

	# oRoot.print_all_1()
	# oRoot.print_all_2()

