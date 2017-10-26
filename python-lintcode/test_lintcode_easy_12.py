# test_lintcode_easy_12.py
# coding: utf-8
'''


给定两个字符串 s 和 t ，确定它们是否是同构的。
两个字符串是同构的如果 s 中的字符可以被替换得到 t。
所有出现的字符必须用另一个字符代替，同时保留字符串的顺序。 没有两个字符可以映射到同一个字符，但一个字符可以映射到自己。
注意事项

你可以假定两个字符串 s 和 t 是一样长度的.
样例

给出 s = "egg", t= "add", 返回 true。
给出 s = "foo", t= "bar", 返回 false。
给出 s = "paper", t= "title", 返回 true。




'''
import collections

def checkSolution(s1,s2):
	s1_list = []
	s2_list = []
	result = 0
	for i in range(len(s1)):
		if i == len(s1)-1:
			if s1[i]==s1[i-1]:
				result += 1
			else:
				s1_list.append(s1[i]+str(1))
		if i!=len(s1)-1 and s1[i] == s1[i+1]:
			result += 1

		else:
			result += 1
			s1_list.append(s1[i]+str(result))
			result = 0
	print s1_list

class Solution(object):  
    def isIsomorphic(self, s, t):  
        s_list = list(s)  
        t_list = list(t)  
        if len(s) != len(t):  
            return False  
        sDict, tDict = {}, {}  
        print zip(s_list,t_list) # This is List 将s字符串和t字符串组成一个列表，如下[('e', 'a'), ('g', 'd'), ('e', 'a'), ('e', 'a')]
        for i, j in zip(s_list, t_list):  
            if i not in sDict:  
                sDict[i] = j  
                print 'sDict--',sDict
            if j not in tDict:  
                tDict[j] = i
                print 'tDict--',tDict  #找出map关系。如下{'e': 'a', 'g': 'd'}， {'a': 'e', 'd': 'g'}
            if tDict[j] != i or sDict[i] != j:  
                return False  #判断两者的对应关系是否一致。

        return True  


if __name__ == '__main__':
	test = Solution()
	print test.isIsomorphic('egeeeas','adaaaep')
	# checkSolution('egg','add')

	# if checkSolution('egg','add') == True:
	# 	print 'Pass'
	# else:
	# 	print 'Fail'
	# if checkSolution('foo','bar') == False:
	# 	print 'Pass'
	# else:
	# 	print 'Fail'
	# if checkSolution('paper','title') == True:
	# 	print 'Pass'
	# else:
	# 	print 'Fail'