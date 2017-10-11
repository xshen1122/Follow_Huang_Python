# # test_xiaobai_95.py
# # coding: utf-8
'''
一个数除了本身之外的因数称为真因数。例如，28的真因数是1、2、4、7和14。这些真因数的和恰好为28，因此我们称28是完全数。

有趣的是，220的真因数之和是284，同时284的真因数之和是220，构成了一个长度为2的链，我们也称之为亲和数对。

有一些更长的序列并不太为人所知。例如，从12496出发，可以构成一个长度为5的链：
12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → …)

由于这条链最后又回到了起点，我们称之为亲和数链。

找出所有元素都不超过一百万的亲和数链中最长的那条，并给出其中最小的那个数。

不是每个数都有亲和数链--估计下面的是某个算法

'''
# def getYinShu(number):
# 	tmp_list = []
# 	for i in range(1,number):
# 		if number%i == 0:
# 			tmp_list.append(i)
# 	return sum(tmp_list)
# def processChain(number):
# 	chain_list = []
# 	orig = number 
# 	chain_list.append(orig)
# 	while True:
		
# 		number = getYinShu(number)
# 		chain_list.append(number)
# 		if orig == number:
# 			break
# 	return chain_list

# if __name__ == '__main__':
# 	for i in range(100,1000000):
# 		print processChain(i)
	
import time as time 

def run():
    MAX = 1000000
    d = [1]*MAX 
    print d
    for i in xrange(2,MAX//2):
        for j in xrange(2*i,MAX,i):
            d[j]+=i 
    max_cl = 0
    for i in xrange(2,MAX):
        n,chain = i,[]
        while d[n]<MAX:
            d[n],n = MAX+1,d[n]
            try:k=chain.index(n)
            except ValueError:chain.append(n)
            else:
                if len(chain[k:]) >max_cl:
                    max_cl,min_link = len(chain[k:]),min(chain[k:])
    print min_link 
t0 = time.time()
run() 
t1 = time.time()
print "running time=",(t1-t0),"s"