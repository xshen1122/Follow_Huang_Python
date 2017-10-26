# test_lintcode_easy_18.py
# coding: utf-8
'''


计算两个数组的交
注意事项

每个元素出现次数得和在数组里一样
答案可以以任意顺序给出
样例

nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].


返回两个数组的交
注意事项

    Each element in the result must be unique.
    The result can be in any order.

样例

nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].



'''
if __name__ == '__main__':
	a = [1,2,2,1]
	b = [2,2]
	print list(frozenset(a).intersection(set(b)))

