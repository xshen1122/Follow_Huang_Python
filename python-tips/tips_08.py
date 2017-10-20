# tips_08.py
# coding: utf-8
'''
time.time()

'''
import time
start = time.time()
for i in range(3000):
    print i
end = time.time()

print start,end
print end - start