# test_lintcode_easy_13.py
# coding: utf-8
'''


Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
样例

Given s = "lintcode", return 0.

Given s = "lovelintcode", return 2.



'''
def findNonRepeating(s):
	for i in range(len(s)):

		for j in range(len(s)): # remove j=i, cannot only compare to i+1 to len(s)
			if j!= i:
				if s[i] == s[j]:
					break
				if s[i] != s[j] and j==len(s)-1:
					return i	
	return -1	
		
			


		

if __name__ == '__main__':

	if findNonRepeating('lintcode') == 0:
		print 'Pass'
	else:
		print 'Fail'
	if findNonRepeating('lovelintcode') == 2:
		print 'Pass'
	else:
		print 'Fail'
	if findNonRepeating('ltltltlt') == -1:
		print 'pass'
	else:
		print 'Fail'