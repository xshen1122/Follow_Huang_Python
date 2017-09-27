# test_callback.py
# coding: utf-8
# coding=utf-8
# 请不要在意为毛要清洁这么多次
'''
可能是学识确实有限，看起来比较懵逼。然后去找了一些通俗易懂的解释--就好像是家政服务，
家政公司提供了一个API：打扫房子，而且还能提供各种打扫，比如扫地，擦家具，清洁马桶等等，
我们把打扫房子看做库函数，那么打扫屋子的方式呢是你自己决定的，
你要怎么打扫就要预约并执行那种回调函数，你预约并执行服务的行为叫做登记回调函数。



'''


def clean1(times):
  """
  就假装是扫地吧，这种函数命名方式，千万别学习
  :param times: 次数
  :return: None
  """
  print '已完成扫地次数:', str(times)


def clean2(times):
  """
  默默的装作洗抽油烟机
  :param times: 次数
  :return: None
  """
  print '已洗抽油烟机次数', str(times)

def clean3(times):
	print 'cook dinner times', str(times)

def clean4(times):
	print 'clean windows times', str(times)
def call_clean(times, function_name):
  """
  这个很重要，这个就是家政公司的业务系统，要啥业务都得在这说
  这个是实现回调函数的核心
  :param times:次数
  :param function_name:回调函数名
  :return:调用的函数结果
  """
  return function_name(times)

if __name__ == '__main__':
  call_clean(100, clean3) # 给我洗100次抽油烟机，好吧，很变态