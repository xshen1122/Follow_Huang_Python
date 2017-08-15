# qukuailian.py
# coding: utf-8
'''
当前最红的概念，区块链技术。
为了比特币，莱特币等虚拟货币服务的，是分布式计算的一种演进

首先将定义块将是什么样子。在区块链中，每个块都存储一个时间戳和一个索引。
在SnakeCoin中，需要把两者都存储起来。
为了确保整个区块链的完整性，每个块都有一个自动识别散列。
与比特币一样，每个块的散列将是块索引、时间戳、数据和前块哈希的加密哈希。数据可以是你想要的任何东西。

重点
1. 块结构的定义， 索引，时间戳，数据，钱块哈希，当前哈希
2. 产生第一个Block0
3. 产生后续19个Block
'''

import hashlib as hasher
 
class Block:
  def __init__(self, index, timestamp, data, previous_hash): #块索引、时间戳、数据和前块哈希的加密哈希
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block() #当前hash
 
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash))
    return sha.hexdigest()
'''
这一步后有块结构，但现在是创建区块链，所以需要向实际的链中添加块。
如前所述，每个块都需要上一个块的信息。但是按照这个说法就有一个问题，
区块链的第一个区块是如何到达那里的呢？不得不说，第一个块，或者说是起源块，
它是一个特殊的块。在很多情况下，它是手动添加的，或者有独特的逻辑允许添加。

'''
import datetime as date
 
def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
 
# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20
 
# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print "Block #{} has been added to the blockchain!".format(block_to_add.index)
  print "Hash: {}\n".format(block_to_add.hash)