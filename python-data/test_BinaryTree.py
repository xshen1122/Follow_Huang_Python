# test_BinaryTree.py
# coding: utf-8
'''
用python实现二叉树


'''

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
 
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
 
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
 
    def getRightChild(self):
        return self.rightChild
 
    def getLeftChild(self):
        return self.leftChild
 
    def setRootVal(self,obj):
        self.key = obj
 
    def getRootVal(self):
        return self.key
 
 
r = BinaryTree('a') #根节点

r.insertLeft('b')

r.insertRight('c')

r.insertLeft('fff')
r.insertLeft('ddd')
print r.getLeftChild().getLeftChild().getLeftChild().getRootVal() # 一整棵树的概念
if r.getRightChild().getRightChild() == None and r.getRightChild().getLeftChild() == None:
	print r.getRightChild().getRootVal(), 'is a leaf Node'
'''
              a
            b    c
        fff
    ddd



'''